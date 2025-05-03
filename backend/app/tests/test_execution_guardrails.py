import pytest
from ai.tools.execution_guardrails import ExecutionGuardrails

def test_validate_query_safe():
    query = "SELECT * FROM users WHERE id = 1"
    assert ExecutionGuardrails.validate_query(query) is True

def test_validate_query_sql_injection():
    query = "SELECT * FROM users; DROP TABLE users;"
    assert ExecutionGuardrails.validate_query(query) is False

def test_enforce_row_limit():
    query = "SELECT * FROM users"
    limited_query = ExecutionGuardrails.enforce_row_limit(query, limit=100)
    assert "LIMIT 100" in limited_query

def test_sanitize_query():
    query = "SELECT * FROM users; -- Drop table"
    sanitized_query = ExecutionGuardrails.sanitize_query(query)
    assert "-- Drop table" not in sanitized_query