from sqlalchemy import Column, Integer, String
from app.core.database import Base
from pydantic import BaseModel

class Prompt(Base):
    __tablename__ = "prompts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)

# Schemas
class PromptCreate(BaseModel):
    title: str
    content: str
    description: str = None

class PromptOut(PromptCreate):
    id: int

    class Config:
        orm_mode = True