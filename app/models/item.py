import logging
from typing import Optional

from pydantic import BaseModel


class generate_answer(BaseModel):
    sysprompt: Optional[str] = None  # Optional field for system prompt
    answer: str


class generate_request(BaseModel):
    input: str
    translate_to: Optional[str] = None  # Optional field to specify a language for translation
