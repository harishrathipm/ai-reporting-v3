import pytest
from ai.agents.intent_classifier_agent import IntentClassifierAgent

def test_intent_classifier_agent():
    agent = IntentClassifierAgent()
    intent = agent.classify_intent("What is the sales data?", {"session": "active"})
    assert intent in ["new_session", "clarification"]