from typing import TypeVar, Type, Generic
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

from Common import Common
from Common.loggerService import LoggerService
from Config import settings

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
                f"@{k} = :{k}"
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

            result = await session.execute(
                text(sql_str),
                params
            )

            rows = result.fetchall()
            column_names = result.keys()

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

                if "TotalQuery" in row_dict and "sVal" in row_dict:
                    self.retCount = row_dict["TotalQuery"] or 0
                    self.retMessage = row_dict["sVal"] or ""

                    if len(row_dict) == 2:
                        continue

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

            await LoggerService.logToDB(
                session,
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