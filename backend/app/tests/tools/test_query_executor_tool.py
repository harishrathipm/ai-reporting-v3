import pytest
from backend.ai.tools.query_executor_tool import QueryExecutorTool

def test_query_executor_tool():
    executor = QueryExecutorTool()
    result = executor.execute_query("SELECT * FROM table1")
    assert result is not None