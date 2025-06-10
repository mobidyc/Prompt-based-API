import logging

from fastapi import APIRouter, Body, Depends, HTTPException, Path
from sqlalchemy.orm import Session

from app.core import crud
from app.core.database import SessionLocal
from app.models.item import generate_answer, generate_request
from app.models.prompt import PromptCreate, PromptOut
from app.services.item_service import generate


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.post("/{prompt_id}/generate", response_model=generate_answer)
def post_prompt_item(
    prompt_id: int = Path(..., description="ID du prompt"),
    payload: generate_request = Body(...),
):
    return generate(prompt_id, payload=payload)


@router.post("/prompts/", response_model=PromptOut)
def create_prompt(
    prompt: PromptCreate,
    db: Session = Depends(get_db),
):
    return crud.create_prompt(db, prompt.title, prompt.content, prompt.description)


@router.get("/prompts/", response_model=list[PromptOut])
def list_prompts(
    db: Session = Depends(get_db),
):
    return crud.get_prompts(db)


@router.delete("/prompts/{prompt_id}", response_model=PromptOut)
def delete_prompt(
    prompt_id: int,
    db: Session = Depends(get_db),
):
    prompt = crud.delete_prompt(db, prompt_id)
    if not prompt:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return prompt
