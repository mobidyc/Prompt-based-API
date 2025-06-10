import logging
from typing import Optional

from sqlalchemy.orm import Session

from app.models import prompt as prompt_models


def get_prompts(db: Session):
    return db.query(prompt_models.Prompt).all()


def get_prompt_by_id(db: Session, prompt_id: int):
    return db.query(prompt_models.Prompt).filter(prompt_models.Prompt.id == prompt_id).first()


def create_prompt(db: Session, title: str, content: str, description: Optional[str] = None):
    prompt = prompt_models.Prompt(title=title, content=content)
    if description is not None:
        prompt.description = description
    db.add(prompt)
    db.commit()
    db.refresh(prompt)
    return prompt


def delete_prompt(db: Session, prompt_id: int):
    prompt = db.get(prompt_models.Prompt, prompt_id)
    if prompt:
        db.delete(prompt)
        db.commit()
    return prompt
