from passlib.context import CryptContext

pwContext = CryptContext(schemes=["bcrypt"], deprecated="auto")

class HashService:
    @staticmethod
    def HashPassword(password : str) -> str:
        return pwContext.hash(password)
    
    @staticmethod
    def VerifyPassword(plainPassword : str, hashedPassword : str) -> bool:
        return pwContext.verify(plainPassword, hashedPassword)