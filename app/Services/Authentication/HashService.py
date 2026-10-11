import bcrypt
import hmac
import hashlib
from app.Config import settings

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

    @staticmethod
    def HashVerificationCode(verifyCode: str) -> str:
        secretKey = settings.email.smtp_secret
        return hmac.new(
            secretKey.encode('utf-8'),
            verifyCode.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()

    @staticmethod
    def VerifyVerificationCode(verifyCode: str, hashedCode: str) -> bool:
        return hmac.compare_digest(
            HashService.HashVerificationCode(verifyCode),
            hashedCode
        )