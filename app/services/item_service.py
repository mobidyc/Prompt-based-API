import logging

from app.models.item import generate_answer


def generate(prompt_id: int) -> generate_answer:
    return generate_answer(id=prompt_id, name=f"Item {prompt_id}", description="This is a test.")
