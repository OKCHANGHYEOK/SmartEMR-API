from pydantic_settings import BaseSettings, SettingsConfigDict

class JWTSettings(BaseSettings):
    secret_key : str
    algorithm : str = "HS256"
    token_expire_minutes : int = 30

    model_config = SettingsConfigDict(
            env_file=".env",
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
    is_home : bool = False

    model_config = SettingsConfigDict(
                    env_file=".env",
                    env_file_encoding="utf-8",
                    env_prefix='DB_',
                    extra="ignore"
                )

class Settings(BaseSettings):
    jwt : JWTSettings = JWTSettings()
    db : DBSesttings = DBSesttings()

settings = Settings()