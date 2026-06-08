import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Config import settings

class CryptoService:
    def _get_cipher() -> Cipher:
        key_bytes = settings.crypto.secret_key.encode('utf-8')
        iv_bytes = settings.crypto.iv.encode('utf-8')

        return Cipher(
            algorithms.AES(key_bytes),
            modes.CBC(iv_bytes),
            backend=default_backend()
        ) 

    def Encrypt(self, plainText : str) -> str:
        """
        문자열을 AES-256-CBC 방식으로 암호화, Base64 인코딩 후 반환
        """

        if not plainText:
            return ""
        
        data_bytes = plainText.encode('utf-8')

        padder = padding.PKCS7(128).padder()
        padder_data = padder.update(data_bytes) + padder.finalize()

        encryptor = self._get_cipher().encryptor()

        encrypted = encryptor.update(padder_data) + encryptor.finalize()

        return base64.b64encode(encrypted).decode('utf-8')
    
    def Decrypt(self, cipherText : str) -> str:
        """
        Base64로 인코딩된 암호문을 복호화하여 원래의 문자열로 반환
        """

        if not cipherText:
            return ""
        
        encrypted = base64.b64decode(cipherText.encode('utf-8'))
        decryptor = self._get_cipher().decryptor()

        padded_data = decryptor.update(encrypted) + decryptor.finalize()

        unpadder = padding.PKCS7(128).unpadder()
        data_bytes = unpadder.update(padded_data) + unpadder.finalize()

        return data_bytes.decode('utf-8')