import pytest
from backend.ai.tools.user_note_integrator_tool import UserNoteIntegratorTool

def test_user_note_integrator_tool():
    integrator = UserNoteIntegratorTool()
    integrator.add_note("table1", "col1", "This is a test note.")
    schema = {"table1": {"col1": "Column description"}}
    enriched_schema = integrator.integrate_notes(schema)
    assert enriched_schema["table1"]["col1"]["note"] == "This is a test note."