import pytest
from ai.agents.clarification_detector_agent import ClarificationDetectorAgent

def test_clarification_detector_agent():
    agent = ClarificationDetectorAgent()
    result = agent.detect_clarification("Can you clarify?", "What is the sales data?")
    assert isinstance(result, bool)