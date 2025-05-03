from backend.ai.agents.global_execution_context import GlobalExecutionContext

def test_global_execution_context():
    context = GlobalExecutionContext("mongodb://localhost:27017", "test_db")
    session = context.create_session("user123")
    assert session["user_id"] == "user123"
    context.delete_session(session["_id"])
    assert context.get_session(session["_id"]) is None