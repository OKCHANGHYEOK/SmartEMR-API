import bcrypt

class HashService:
    @staticmethod
    def HashPassword(password : str) -> str:
        # 비밀번호를 바이트로 인코딩
        passwordBytes = password.encode('utf-8')

        # 솔트 생성
        salt = bcrypt.gensalt()

        # 해싱
        hashed = bcrypt.hashpw(passwordBytes, salt)

        return hashed.decode('utf-8')
    
    @staticmethod
    def VerifyPassword(plainPW : str, hashedPW : str):
        return bcrypt.checkpw(
            plainPW.encode('utf-8'),
            hashedPW.encode('utf-8')
        )
        