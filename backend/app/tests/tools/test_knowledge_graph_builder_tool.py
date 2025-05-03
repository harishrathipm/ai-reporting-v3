import pytest
from backend.ai.tools.knowledge_graph_builder_tool import KnowledgeGraphBuilderTool

def test_knowledge_graph_builder():
    schema = {"table1": ["col1", "col2"]}
    builder = KnowledgeGraphBuilderTool()
    graph = builder.build_graph(schema)
    assert "table1" in graph
    builder.add_relationship("table1", "table2", "one-to-many")
    assert len(graph["table1"]["relationships"]) == 1