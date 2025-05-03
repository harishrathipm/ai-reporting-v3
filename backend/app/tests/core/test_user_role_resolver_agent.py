import pytest
from backend.ai.agents.user_role_resolver_agent import UserRoleResolverAgent
from unittest.mock import MagicMock

@pytest.fixture
def mock_llm():
    mock = MagicMock()
    mock.generate_response.side_effect = lambda prompt: "Executive" if "role" in prompt else "Analyst"
    return mock

def test_user_role_resolver_agent(mock_llm):
    agent = UserRoleResolverAgent()
    agent.llm = mock_llm
    role = agent.resolve_role("What is the sales data?")
    assert role == "Executive"