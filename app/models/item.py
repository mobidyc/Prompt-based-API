import logging
from typing import Optional

from pydantic import BaseModel


class generate_answer(BaseModel):
    sysprompt: Optional[str] = None  # Optional field for system prompt
    answer: str


class request_variables(BaseModel):
    language: Optional[str] = None  # Language for the request, e.g., "en" for English, "fr" for French


class generate_request(BaseModel):
    input: str
    variables: Optional[request_variables] = None  # Optional field to use a custom variables object
