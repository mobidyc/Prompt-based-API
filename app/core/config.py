import logging

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = Field(default="Mon API")
    DEBUG: bool = Field(default=True)
    DATABASE_URL: str = Field(default="sqlite:///./prompts.db")
    OPENAI_API_KEY: str = Field(default="Please fill this variable in the .env file, with your OpenAI SDK key")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
