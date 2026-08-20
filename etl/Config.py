from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

base_dir = Path(__file__).resolve().parent

class ETLSettings(BaseSettings):
    api_url : str
    service_key : str
    exclude_keyword : list

    model_config = SettingsConfigDict(
        env_file=f"{base_dir}/.env",
        env_file_encoding="utf-8",
        env_prefix="HIRA_",
        extra="ignore"
    )

settings = ETLSettings()    