import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Config import settings

class CryptoService:
    
    @staticmethod
    def _get_cipher() -> Cipher:  # <-- @staticmethod 추가
        key_bytes = settings.crypto.secret_key.encode('utf-8')
        iv_bytes = settings.crypto.iv.encode('utf-8')

        return Cipher(
            algorithms.AES(key_bytes),
            modes.CBC(iv_bytes),
            backend=default_backend()
        ) 

    @staticmethod
    def Encrypt(plainText : str) -> str:  # <-- self 제거 및 @staticmethod 추가
        """
        문자열을 AES-256-CBC 방식으로 암호화, Base64 인코딩 후 반환
        """
        if not plainText:
            return ""
        
        data_bytes = plainText.encode('utf-8')

        padder = padding.PKCS7(128).padder()
        padder_data = padder.update(data_bytes) + padder.finalize()

        # self._get_cipher() 대신 클래스 메서드로 직접 호출합니다.
        encryptor = CryptoService._get_cipher().encryptor()

        encrypted = encryptor.update(padder_data) + encryptor.finalize()

        return base64.b64encode(encrypted).decode('utf-8')
    
    @staticmethod
    def Decrypt(cipherText : str) -> str:  # <-- 복호화도 동일하게 self 제거 및 정적 처리
        """
        Base64로 인코딩된 암호문을 복호화하여 원래의 문자열로 반환
        """
        if not cipherText:
            return ""
            
        # 필요시 복호화 로직 채워넣기
        ...