from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

base_dir = Path(__file__).resolve().parent
env_url = f"{base_dir}/.env"

class JWTSettings(BaseSettings):
    secret_key : str
    algorithm : str = "HS256"
    token_expire_minutes : int = 30
    refresh_token_expire_days : int = 14

    model_config = SettingsConfigDict(
            env_file=env_url,
            env_file_encoding="utf-8",
            env_prefix='JWT_',
            extra="ignore"
        )

class DBSesttings(BaseSettings):
    ip : str = ""
    user : str 
    pw : str
    name : str
    port : str
    echo : bool
    ishome : bool = False

    model_config = SettingsConfigDict(
                    env_file=env_url,
                    env_file_encoding="utf-8",
                    env_prefix='DB_',
                    extra="ignore"
                )
    
class CryptoSettings(BaseSettings):
    secret_key : str
    iv : str    

    model_config = SettingsConfigDict(
            env_file=env_url,
            env_file_encoding="utf-8",
            env_prefix='CRYPTO_',
            extra="ignore"
        )
    
class NaverPaySettings(BaseSettings):
    apply_url : str
    client_id : str
    client_secret : str
    chain_id : str

    model_config = SettingsConfigDict(
            env_file=env_url,
            env_file_encoding="utf-8",
            env_prefix='NAVERPAY_',
            extra="ignore"
        )    

class EmailSettings(BaseSettings):
    smtp_host : str
    smtp_port : int
    smtp_user : str
    smtp_password : str
    smtp_from : str

    model_config = SettingsConfigDict(
        env_file=env_url,
        env_file_encoding="utf-8",
        env_prefix='EMAIL_',
        extra="ignore"
    )

class Settings(BaseSettings):
    jwt : JWTSettings = JWTSettings()
    db : DBSesttings = DBSesttings()
    naverpay : NaverPaySettings = NaverPaySettings()
    crypto : CryptoSettings = CryptoSettings()
    email : EmailSettings = EmailSettings()

settings = Settings()