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

class Settings(BaseSettings):
    jwt : JWTSettings = JWTSettings()
    db : DBSesttings = DBSesttings()
    crypto : CryptoSettings = CryptoSettings()

settings = Settings()