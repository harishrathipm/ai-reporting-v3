import pytest
from backend.ai.agents.role_to_entity_access_agent import RoleToEntityAccessAgent
from unittest.mock import MagicMock

@pytest.fixture
def mock_llm():
    mock = MagicMock()
    mock.generate_response.side_effect = lambda prompt: "table1,table2"
    return mock

def test_role_to_entity_access_agent(mock_llm):
    agent = RoleToEntityAccessAgent()
    agent.llm = mock_llm
    entities = agent.get_accessible_entities("Executive")
    assert entities == ["table1", "table2"]