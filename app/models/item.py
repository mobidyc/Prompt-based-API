import logging

from pydantic import BaseModel


class generate_answer(BaseModel):
    id: int
    name: str
    description: str
