import logging

from pydantic import BaseModel


class generate_answer(BaseModel):
    answer: str


class generate_request(BaseModel):
    input: str
