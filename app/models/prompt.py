import logging
from typing import Optional

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String

from app.core.database import Base


class Prompt(Base):
    __tablename__ = "prompts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)


class PromptCreate(BaseModel):
    title: str
    content: str
    description: Optional[str] = None


class PromptOut(PromptCreate):
    id: int

    class Config:
        orm_mode = True
