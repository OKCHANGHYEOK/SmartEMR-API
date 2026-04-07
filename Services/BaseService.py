from Infrastructure import AppDBContext

class BaseSerivce:
    def __init__(self, dbContext : AppDBContext, session):
        self.dbContext = dbContext
        self.session = session