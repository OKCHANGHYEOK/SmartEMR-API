from typing import TypeVar, Type, Generic
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from aioodbc.cursor import Cursor

from app.Common import Common
from app.Common.loggerService import LoggerService
from app.Config import settings

TReq = TypeVar("TReq")
TRes = TypeVar("TRes")


class AppDBContext:
    retMessage = ""
    retCount = 0
    retIsSuccess = False

    def __init__(self, logger=None):
        self.logger = logger or LoggerService.getLogger()

        connection_str = self.__getDBConnectionString()
        echo_mode = settings.db.echo is True

        self.engine = create_async_engine(
            f"mssql+aioodbc:///?odbc_connect={connection_str}",
            echo=echo_mode,
            future=True
        )

        self.AsyncSessionLocal : async_sessionmaker[AsyncSession] = sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False
        )

    # ==========================================================
    # Public API
    # ==========================================================

    @property
    def GetItem(self) -> TRes:
        return self.QueryFactory(self, True)

    @property
    def GetItems(self) -> list[TRes]:
        return self.QueryFactory(self, False)

    # ==========================================================
    # Internal Query Methods
    # ==========================================================

    async def _GetItem(self, 
                       proc_name: str, 
                       request_obj: TReq, 
                       response_type: Type[TRes],
                       session : AsyncSession | None = None) -> TRes | None:
        rows = await self._ExecuteQuery(proc_name, request_obj, response_type, session)

        return rows[0] if rows else None

    async def _GetItems(self, 
                        proc_name: str, 
                        request_obj: TReq, 
                        response_type: Type[TRes],
                        session : AsyncSession | None = None) -> list[TRes]:
        return await self._ExecuteQuery(proc_name, request_obj, response_type, session)


    async def _ExecuteQuery(self,
                            proc_name: str,
                            request_obj: TReq,
                            response_type: Type[TRes],
                            session: AsyncSession | None = None) -> list[TRes]:

        own_session = session is None

        if own_session:
            session = self.AsyncSessionLocal()

        params = {}

        try:
            self.retIsSuccess = False
            self.retCount = 0
            self.retMessage = ""

            self.logger.debug(
                f"Executing Procedure: {proc_name}"
            )

            proc_name = str(proc_name).split("eSP.")[1]

            annotations = getattr(
                request_obj,
                "__annotations__",
                {}
            )

            for k, v in request_obj.__dict__.items():
                if k.startswith("_"):
                    continue

                if v is None:
                    field_type = annotations.get(k, str)

                    if (
                        field_type is str
                        or (
                            hasattr(field_type, "__args__")
                            and str in field_type.__args__
                        )
                    ):
                        v = ""
                    else:
                        v = 0

                params[k] = v

            param_placeholders = ", ".join(
                f"@{k} = ?"
                for k in params.keys()
            )

            sql_str = f"""
                DECLARE @t int,
                        @s nvarchar(250);

                EXEC [dbo].[{proc_name}]
                    {param_placeholders},
                    @TotalQuery = @t OUTPUT,
                    @sVal = @s OUTPUT;

                SELECT
                    @t AS TotalQuery,
                    @s AS sVal;
            """

            # 커넥션 생성 및 sql 실행
            conn = await session.connection()
            raw_conn = await conn.get_raw_connection()

            db_conn = raw_conn.driver_connection 

            cursor : Cursor = await db_conn.cursor() 

            await cursor.execute(sql_str, tuple(params.values()))

            rows = []
            column_names = []

            if cursor.description:
                rows = await cursor.fetchall()
                column_names = [column[0] for column in cursor.description]

            while await cursor.nextset():
                if not cursor.description:
                    continue

                output_rows = await cursor.fetchall()

                if output_rows:
                    output_columns = [col[0] for col in cursor.description]
                    output_dict = dict(zip(output_columns, output_rows[0]))

                    self.retCount = output_dict.get("TotalQuery") or 0
                    self.retMessage = output_dict.get("sVal") or ""

            # 외부에서 Session을 전달받은 경우에는
            # 여기서 commit하지 않는다.
            if own_session:
                await session.commit()

            if not rows:
                self.retIsSuccess = True
                return []

            arr_map: list[TRes] = []

            for row in rows:
                row_dict = dict(zip(column_names, row))

                item = response_type(**row_dict)
                arr_map.append(item)

            self.retIsSuccess = True

            self.logger.info(
                f"Successfully executed {proc_name}"
            )

            return arr_map

        except Exception as e:
            # Session을 직접 생성한 경우에만
            # 여기서 rollback한다.
            if own_session:
                await session.rollback()

            self.logger.error(
                f"DB Error: {e}",
                exc_info=True
            )

            # 로깅용 세션은 다른 프로시저 호출시의 세션과 별개로 처리
            await LoggerService.logToDB(
                self.AsyncSessionLocal(),
                proc_name,
                params,
                e
            )

            raise

        finally:
            # Session을 직접 생성한 경우에만 종료한다.
            if own_session:
                await session.close()

    # ==========================================================
    # Internal Classes
    # ==========================================================

    class QueryBuilder(Generic[TRes]):
        def __init__(self, db : AppDBContext, response_type: Type[TRes], is_single: bool):
            self.db = db
            self.response_type = response_type
            self.is_single = is_single

        async def __call__(self, proc_name: str, request_obj, session : AsyncSession | None = None) -> TRes | list[TRes] | None:
            if self.is_single:
                return await self.db._GetItem(proc_name, request_obj, self.response_type, session)

            return await self.db._GetItems(proc_name, request_obj, self.response_type, session)

    class QueryFactory:
        def __init__(self, db : AppDBContext, is_single: bool):
            self.db = db
            self.is_single = is_single

        def __getitem__(self, response_type: Type[TRes]) -> "AppDBContext.QueryBuilder[TRes]":
            return AppDBContext.QueryBuilder(self.db, response_type, self.is_single)

    # ==========================================================
    # DB Connection
    # ==========================================================

    def __getDBConnectionString(self):
        currentIP = (
            settings.db.ip
            if settings.db.ishome
            else Common.getLocalIP()
        )

        return (
            f"Driver={{ODBC Driver 17 for SQL Server}};"
            f"Server={currentIP},{settings.db.port};"
            f"Database={settings.db.name};"
            f"UID={settings.db.user};"
            f"PWD={settings.db.pw};"
        )