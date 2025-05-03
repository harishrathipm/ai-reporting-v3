import pytest
from backend.ai.agents.temp_storage import TempStorage

@pytest.fixture
def temp_storage():
    return TempStorage("mongodb://localhost:27017", "test_db")

def test_temp_storage(temp_storage):
    temp_storage.store_data("session1", "step1", {"key": "value"})
    data = temp_storage.retrieve_data("session1", "step1")
    assert data["data"] == {"key": "value"}
    temp_storage.delete_data("session1")
    assert temp_storage.retrieve_data("session1", "step1") is None