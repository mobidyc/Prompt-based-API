import logging

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.api.v1.routes import items

app = FastAPI()
app.include_router(items.router)
client = TestClient(app)


@pytest.fixture
def prompt_data():
    return {
        "title": "Translate EN->FR",
        "content": "Translate the following sentence from English to French: {sentence}",
    }


@pytest.fixture
def prompt_id(prompt_data):
    resp = client.post("/prompts/", json=prompt_data)
    return resp.json()["id"]


def test_create_prompt(prompt_data):
    response = client.post("/prompts/", json=prompt_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == prompt_data["title"]
    assert data["content"] == prompt_data["content"]
    assert "id" in data


def test_list_prompts(prompt_data):
    client.post("/prompts/", json=prompt_data)
    response = client.get("/prompts/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(prompt["title"] == prompt_data["title"] for prompt in data)


def test_delete_prompt(prompt_data):
    create_resp = client.post("/prompts/", json=prompt_data)
    prompt_id = create_resp.json()["id"]
    delete_resp = client.delete(f"/prompts/{prompt_id}")
    assert delete_resp.status_code == 200
    deleted = delete_resp.json()
    assert deleted["id"] == prompt_id
    delete_resp2 = client.delete(f"/prompts/{prompt_id}")
    assert delete_resp2.status_code == 404


def test_translate_english_to_french(prompt_id):
    payload = {"input": "Hello, how are you?", "variables": {"language": "fr"}}
    response = client.post(f"/{prompt_id}/generate", json=payload)
    assert response.status_code == 200
    data = response.json()

    assert "answer" in data
    assert isinstance(data["answer"], str)
    assert "Bonjour" in data["answer"] or "Comment" in data["answer"]
