import pytest
from backend.ai.agents.step_local_state import StepLocalState

@pytest.fixture
def step_local_state():
    return StepLocalState("mongodb://localhost:27017", "test_db")

def test_step_local_state(step_local_state):
    step_local_state.log_step("session1", {"step": 1, "data": "test"})
    steps = step_local_state.get_steps("session1")
    assert len(steps) == 1
    step_local_state.delete_steps("session1")
    assert len(step_local_state.get_steps("session1")) == 0