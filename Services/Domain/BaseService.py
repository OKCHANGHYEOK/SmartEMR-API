from fastapi import Depends
from Infrastructure import AppDBContext

class BaseSerivce:
    def __init__(self, dbContext : AppDBContext = Depends(AppDBContext)):
        self.DbContext = dbContext