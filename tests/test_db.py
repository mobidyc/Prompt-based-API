import logging

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.api.v1.routes.items import router
from app.models.prompt import PromptCreate

app = FastAPI()
app.include_router(router)

client = TestClient(app)


@pytest.fixture
def prompt_data():
    return {"title": "Test Prompt", "content": "This is a test prompt content."}


def test_create_prompt(prompt_data):
    response = client.post("/prompts/", json=prompt_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == prompt_data["title"]
    assert data["content"] == prompt_data["content"]
    assert "id" in data


def test_list_prompts(prompt_data):
    # Ensure at least one prompt exists
    client.post("/prompts/", json=prompt_data)
    response = client.get("/prompts/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(prompt["title"] == prompt_data["title"] for prompt in data)


def test_delete_prompt(prompt_data):
    # Create a prompt to delete
    create_resp = client.post("/prompts/", json=prompt_data)
    prompt_id = create_resp.json()["id"]
    # Delete the prompt
    delete_resp = client.delete(f"/prompts/{prompt_id}")
    assert delete_resp.status_code == 200
    deleted = delete_resp.json()
    assert deleted["id"] == prompt_id
    # Try to delete again, should 404
    delete_resp2 = client.delete(f"/prompts/{prompt_id}")
    assert delete_resp2.status_code == 404
