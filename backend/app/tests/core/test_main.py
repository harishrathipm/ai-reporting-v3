import pytest
from backend.app.main import app

def test_main():
    response = app.test_client().get("/")
    assert response.status_code == 200