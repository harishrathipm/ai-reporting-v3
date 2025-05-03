import pytest
from ai.agents.global_execution_context import GlobalExecutionContext
from sqlalchemy import create_engine, text
from app.main import engine

@pytest.fixture
def global_execution_context():
    return GlobalExecutionContext("mongodb://localhost:27017", "test_db")

@pytest.fixture(scope="module")
def setup_test_sqlalchemy():
    """Fixture to set up and tear down the SQLAlchemy test database."""
    # Create tables and insert test data
    with engine.connect() as connection:
        connection.execute(text("CREATE TABLE test_table (id INTEGER PRIMARY KEY, value TEXT)"))
        connection.execute(text("INSERT INTO test_table (id, value) VALUES (1, 'Test Value')"))
    yield
    # Drop tables after tests
    with engine.connect() as connection:
        connection.execute(text("DROP TABLE test_table"))

def test_global_execution_context(global_execution_context):
    context = global_execution_context
    session = context.create_session("user123")
    assert session["user_id"] == "user123"
    context.delete_session(session["_id"])
    assert context.get_session(session["_id"]) is None

def test_global_execution_context_with_sqlalchemy(setup_test_sqlalchemy):
    """Test GlobalExecutionContext with SQLAlchemy integration."""
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM test_table")).fetchall()
        assert len(result) == 1
        assert result[0]["value"] == "Test Value"