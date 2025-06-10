from fastapi import APIRouter
from app.models.item import generate_answer
from app.services.item_service import generate

router = APIRouter()

@router.post("/{prompt_id}/generate", response_model=generate_answer)
def post_prompt_item(prompt_id: int):
    return generate(prompt_id)
