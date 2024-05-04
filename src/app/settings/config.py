from functools import lru_cache

from pydantic_settings import BaseSettings, EnvSettingsSource, SettingsConfigDict
from pydantic import Field


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file='../.env')
    postgres_connection_uri: str = Field(alias='POSTGRES_CONNECTION_URI')
    pythonpath: str = Field(alias='pythonpath')
    api_port: int = Field(alias='API_PORT')
    db_password: str = Field(alias='DB_PASSWORD')
    postgres_db: str = Field(alias='POSTGRES_DB')
    postgres_user: str = Field(alias='POSTGRES_USER')
    postgres_host: str = Field(alias='POSTGRES_HOST')
