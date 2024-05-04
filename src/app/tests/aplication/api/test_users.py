import re
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
import httpx


@pytest.mark.asyncio
async def test_create_user_success(
        app: FastAPI,
        client: TestClient
):
    url = app.url_path_for('create_user_handler')
    response: httpx.Response = client.post(url=url, json={'email': 'a@gmail.com', 'password': 'Aa.65sajdh'})
    assert response.status_code == 201
    json_response = response.json()
    assert json_response['email'] == 'a@gmail.com'
    assert re.match(r'^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}\Z', json_response['oid']) is not None


@pytest.mark.asyncio
async def test_create_user_already_exists(
        app: FastAPI,
        client: TestClient
):
    url = app.url_path_for('create_user_handler')
    response: httpx.Response = client.post(url=url, json={'email': 'a@gmail.com', 'password': 'Aa.65sajdh'})
    assert response.status_code == 201
    json_response = response.json()
    assert json_response['email'] == 'a@gmail.com'
    assert re.match(r'^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}\Z', json_response['oid']) is not None

    response: httpx.Response = client.post(url=url, json={'email': 'a@gmail.com', 'password': 'Aasdf.65sajdh'})
    assert response.status_code == 400
    json_response = response.json()
    assert json_response['detail']['error'] == 'Пользователь с почтой <a@gmail.com> уже сущесвует'
    assert re.match(r'^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}\Z', json_response['oid']) is not None