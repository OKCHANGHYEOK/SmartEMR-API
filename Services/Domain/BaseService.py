from Infrastructure import AppDBContext

class BaseSerivce:
    def __init__(self, dbContext : AppDBContext):
        self.DbContext = dbContext