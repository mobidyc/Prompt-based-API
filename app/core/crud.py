from sqlalchemy.orm import Session
from app.models import prompt as prompt_models

def get_prompts(db: Session):
    return db.query(prompt_models.Prompt).all()

def create_prompt(db: Session, title: str, content: str):
    prompt = prompt_models.Prompt(title=title, content=content)
    db.add(prompt)
    db.commit()
    db.refresh(prompt)
    return prompt

def delete_prompt(db: Session, prompt_id: int):
    prompt = db.query(prompt_models.Prompt).get(prompt_id)
    if prompt:
        db.delete(prompt)
        db.commit()
    return prompt
