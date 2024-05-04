import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.application.api.main import create_app
from app.logic import init_container
from app.tests.fixtues import init_dumpy_container


@pytest.fixture
def app() -> FastAPI:
    app = create_app()
    app.dependency_overrides[init_container] = init_dumpy_container
    return app


@pytest.fixture
def client(app: FastAPI) -> TestClient:
    return TestClient(app)
