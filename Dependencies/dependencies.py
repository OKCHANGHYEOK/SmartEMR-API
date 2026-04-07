from Infrastructure import AppDBContext
from Common import LoggerService

_AppDBContext = AppDBContext()
_loggerService = LoggerService.getLogger()

async def GetDBSession():
    async with _AppDBContext.AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
