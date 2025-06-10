import logging

from openai import OpenAI

from app.core.config import settings
from app.core.crud import get_prompt_by_id
from app.core.database import SessionLocal
from app.models.item import generate_answer, generate_request

client = OpenAI(api_key=settings.OPENAI_API_KEY)

# Create a DB session
db = SessionLocal()


def generate(prompt_id: int, payload: generate_request) -> generate_answer:
    # Retrieve the prompt
    prompt = get_prompt_by_id(db, prompt_id)

    if payload is None or payload.input is None:
        raise Exception("Payload is missing or invalid")

    if prompt is None or prompt.id is None:
        raise Exception("Prompt not found")

    sysprompt = str(prompt.content)  # cast to str as it can be a non-string type
    if payload.translate_to is not None:
        sysprompt = f"{str(prompt.content)} Translate the following text to {payload.translate_to}."

    response = client.responses.create(model="gpt-4.1", input=f"{sysprompt}\n\n{payload.input} ")

    return generate_answer(sysprompt=sysprompt, answer=f"{response.output_text}")
