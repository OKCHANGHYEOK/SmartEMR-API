from fastapi import Depends
from Infrastructure import AppDBContext

class BaseService:
    _dbContext : AppDBContext = AppDBContext()

    @property
    def DbContext(self) -> AppDBContext:
        return self._dbContext