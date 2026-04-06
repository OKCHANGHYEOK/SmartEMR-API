import logging
import os
import traceback
import json
from logging.handlers import TimedRotatingFileHandler
from Common import common as Common
from sqlalchemy import text

class LoggerService:
    _logger = None

    @classmethod
    def getLogger(cls, name="Logger"):
        if cls._logger is None:
            cls._logger = cls.setLogger(name)
        return cls._logger

    @staticmethod
    def setLogger(name):
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        # 로그 저장 폴더 생성
        logDir = "Logs"

        if not os.path.exists(logDir):
            os.makedirs(logDir)

        # 포맷 설정
        formatter = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # 핸들러 설정 - 콘솔 출력
        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(formatter)
        consoleHandler.setLevel(logging.INFO)

        # 핸들러 설정 - 파일 저장용 
        logFileName = os.path.join(logDir, "app.log")
        fileHandler = TimedRotatingFileHandler(
            filename=logFileName,
            when="midnight",
            backupCount=30,
            encoding="utf-8"
        )

        fileHandler.setFormatter(formatter)
        fileHandler.setLevel(logging.DEBUG)

        # 로거에 핸들러 등록
        logger.addHandler(consoleHandler)
        logger.addHandler(fileHandler)

        return logger
    
    @staticmethod
    async def logToDB(session, proc_name, entity_dict, exception):
        """
        DB 세션을 전달받아 AppErrorLog 테이블에 에러 기록
        """
        try:
            errorType = type(exception).__name__
            errorMessage = str(exception)
            stackTrace = traceback.format_exc()
            
            paramJson = json.dumps(entity_dict, default=str, ensure_ascii=False)

            setItem = {
                "ProcedureName": proc_name,
                "InputParams": paramJson,
                "ErrorType": errorType,
                "ErrorMessage": errorMessage,
                "StackTrace": stackTrace,
                "ServerIP": Common.getLocalIP()
            }

            sql_str = """
                INSERT INTO [dbo].[AppErrorLog] 
                (OccurredAt, ProcedureName, InputParams, ErrorType, ErrorMessage, StackTrace, ServerIP)
                VALUES 
                (SYSDATETIME(), :ProcedureName, :InputParams, :ErrorType, :ErrorMessage, :StackTrace, :ServerIP)
            """
            
            await session.execute(text(sql_str), setItem)
            await session.commit()
            
            # DB 저장 성공 여부도 파일 로그에 남기면 추적하기 좋음
            # logger.info(f"Error log saved to DB for {proc_name}")

        except Exception as e:
            # 로그 저장 자체에서 에러가 나면 '파일 로그'에만 남기고 조용히 종료 (무한 루프 방지)
            print(f"Failed to save error log to DB: {e}")
