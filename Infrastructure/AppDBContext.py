import Common.common as Common
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from Common.loggerService import LoggerService
from fastapi import Depends
from Config import settings

class AppDBContext:
    retMessage = "" 
    retCount = 0
    retIsSuccess = False

    def __init__(self, logger = None):
        self.logger = logger or LoggerService.getLogger()

        connection_str = self.__getDBConnectionString()
        echo_mode = settings.db.echo == True

        # 비동기 엔진 생성
        self.engine = create_async_engine(
            f"mssql+aioodbc:///?odbc_connect={connection_str}",
            echo=echo_mode, # SQL 실행 로그를 터미널에 출력 (디버깅용)
            future=True
        )

        # 비동기 전용 세션 생성기 설정
        self.AsyncSessionLocal = sessionmaker(
            bind=self.engine, 
            class_=AsyncSession, 
            expire_on_commit=False
        )

    def __getDBConnectionString(self):
        if settings.db.is_home == True:
            currentIP = settings.db.ip
        else:    
            currentIP = Common.getLocalIP()

        dbUser = settings.db.user
        dbPW = settings.db.pw
        dbName = settings.db.name
        dbPort = settings.db.port

        connectionStr = (
            f"Driver={{ODBC Driver 17 for SQL Server}};"
            f"Server={currentIP},{dbPort};"
            f"Database={dbName};"
            f"UID={dbUser};"
            f"PWD={dbPW};"
        ) 

        return connectionStr

    async def GetItem[T](self, proc_name, entity_obj : T) -> T:
        """
        저장 프로시저를 비동기로 호출하는 공용 메서드 - 단일 항목 반환
        """
        ret = await self._ExecuteQuery(proc_name, entity_obj)

        if isinstance(ret, list):
            return ret[0] if len(ret) > 0 else None
        
        return ret

    async def GetItems[T](self, proc_name, entity_obj : T) -> list[T]:
        """
        저장 프로시저를 비동기로 호출하는 공용 메서드 - 리스트 반환
        """
        ret = await self._ExecuteQuery(proc_name, entity_obj)
        
        return ret if ret else []
            
    async def _ExecuteQuery[T](self, proc_name, entity_obj : T) -> T | list[T] | None:
        async with self.AsyncSessionLocal() as session:
            try:
                self.retIsSuccess = False

                # 실행 정보 로그 (DEBUG)
                self.logger.debug(f"Executing Procedure: {proc_name}")

                # 프로시저 호출명 전처리
                proc_name = str(proc_name).split("eSP.")[1]

                # 엔티티 객체에서 내부 필드 제외하고 파라미터 추출
                params = {k: v for k, v in entity_obj.__dict__.items() if not k.startswith('_')}
                
                # 파라미터 동적 생성 (@param = :param)
                param_placeholders = ", ".join([f"@{k} = :{k}" for k in params.keys()])
                
                # SQL 문 조립
                sql_str = f"""
                    DECLARE @t int, @s nvarchar(250);
                    EXEC [dbo].[{proc_name}] 
                        {param_placeholders},
                        @TotalQuery = @t OUTPUT,
                        @sVal = @s OUTPUT;
                    SELECT @t as TotalQuery, @s as sVal;
                """

                sql = text(sql_str)

                # 실행 (비동기 방식)
                result = await session.execute(sql, params)
                
                # 프로시저 내부에서 변경이 일어난다면 커밋
                await session.commit()
                
                # 실행 결과 로깅
                self.logger.info(f"Successfully executed {proc_name}")

                # 결과 데이터 추출
                rows = result.fetchall()                
                column_names = result.keys()

                # 결과행이 업으면 None 반환
                if not rows:
                    self.retIsSuccess = True
                    return None
                
                # 엔티티 매핑 및 결과 생성
                entityType = type(entity_obj)
                arrMap = []
                totalQueryVal = 0
                sVal = ""

                for row in rows:
                    # 각 로우를 딕셔너리 변환 -> 엔티티 객체 생성
                    row_dict = dict(zip(column_names, row))

                    if "TotalQuery" in row_dict and "sVal" in row_dict:
                        totalQueryVal = row_dict["TotalQuery"]
                        sVal = row_dict["sVal"]

                        if len(row_dict) == 2: continue

                    item = entityType(**row_dict)
                    arrMap.append(item)

                # 전역필드값 설정
                self.retMessage = sVal if sVal else ""
                self.retCount = totalQueryVal
                self.retIsSuccess = True            

                return arrMap[0] if len(arrMap) == 1 else arrMap
                
            except Exception as e:
                await session.rollback()
                
                # 파일 로그
                self.logger.error(f"DB Error: {e}", exc_info=True)
            
                # DB 로그 
                params_dict = {k: v for k, v in entity_obj.__dict__.items() if not k.startswith('_')}

                await LoggerService.logToDB(session, proc_name, params_dict, e)

                raise e