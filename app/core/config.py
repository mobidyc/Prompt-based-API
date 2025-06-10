import logging

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = Field(default="Mon API")
    DEBUG: bool = Field(default=True)
    DATABASE_URL: str = Field(default="sqlite:///./prompts.db")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings(_env_file=".env", _env_file_encoding="utf-8")
