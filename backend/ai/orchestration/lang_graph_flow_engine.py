from langchain.graph import Graph
from langchain.agents import Tool
from ai.tools.knowledge_graph_builder_tool import KnowledgeGraphBuilderTool, TavilyWebSearchTool
from ai.tools.query_execution_tool_selector import QueryExecutionToolSelector
from ai.tools.execution_guardrails import ExecutionGuardrails
from ai.tools.result_metadata_tracker import ResultMetadataTracker

class LangGraphFlowEngine:
    def __init__(self, tavily_api_key):
        self.graph = Graph()
        self.tavily_tool = TavilyWebSearchTool(api_key=tavily_api_key)
        self.knowledge_graph_tool = KnowledgeGraphBuilderTool()
        self.query_selector = QueryExecutionToolSelector()
        self.guardrails = ExecutionGuardrails()
        self.metadata_tracker = ResultMetadataTracker()

        self._register_tools()

    def _register_tools(self):
        """
        Registers tools into the LangChain graph for orchestration.
        """
        self.graph.add_tool(Tool(name="TavilyWebSearch", func=self.tavily_tool.search, description="Perform web searches using Tavily."))
        self.graph.add_tool(Tool(name="KnowledgeGraphBuilder", func=self.knowledge_graph_tool.build_graph, description="Build a knowledge graph from schema."))
        self.graph.add_tool(Tool(name="QueryExecutionSelector", func=self.query_selector.select_tool, description="Select the appropriate tool for query execution."))
        self.graph.add_tool(Tool(name="ExecutionGuardrails", func=self.guardrails.validate_query, description="Validate SQL queries for safety."))
        self.graph.add_tool(Tool(name="ResultMetadataTracker", func=self.metadata_tracker.log_step_metadata, description="Log metadata for query execution steps."))

        # New tools for clarification and output formatting
        self.graph.add_tool(Tool(name="ClarificationHandler", func=self._handle_clarification, description="Handle user clarifications and replan queries."))
        self.graph.add_tool(Tool(name="OutputFormatter", func=self._format_output, description="Format insights and visualizations for delivery."))

    def _handle_clarification(self, user_feedback, current_plan):
        """
        Handles user clarifications and replans the query.

        Args:
            user_feedback (str): The user's clarification or feedback.
            current_plan (dict): The current query plan.

        Returns:
            dict: The updated query plan.
        """
        # Placeholder logic for handling clarifications
        self.metadata_tracker.log_step_metadata({"step_id": "clarification", "feedback": user_feedback}, {"status": "processed"})
        return {"updated_plan": True, "details": "Replanned based on feedback."}

    def _format_output(self, insights, visualizations):
        """
        Formats insights and visualizations for delivery.

        Args:
            insights (str): The generated insights.
            visualizations (dict): The visualization configurations.

        Returns:
            dict: The formatted output ready for delivery.
        """
        # Placeholder logic for formatting output
        formatted_output = {
            "insights": insights,
            "visualizations": visualizations,
            "status": "formatted"
        }
        self.metadata_tracker.log_step_metadata({"step_id": "output_formatting"}, {"status": "success"})
        return formatted_output

    def execute_flow(self, user_query, schema):
        """
        Executes the flow for a given user query and schema.

        Args:
            user_query (str): The user's natural language query.
            schema (dict): The database schema.

        Returns:
            dict: The final result of the flow.
        """
        # Step 1: Build the knowledge graph
        knowledge_graph = self.knowledge_graph_tool.build_graph(schema)

        # Step 2: Perform a web search for additional context
        web_search_results = self.tavily_tool.search(user_query)

        # Step 3: Validate the query using guardrails
        if not self.guardrails.validate_query(user_query):
            raise ValueError("Query validation failed due to potential SQL injection or complexity.")

        # Step 4: Select the appropriate tool for execution
        selected_tool = self.query_selector.select_tool({"db_type": "sql"})

        # Step 5: Log metadata for the step
        self.metadata_tracker.log_step_metadata({"step_id": 1, "tool": selected_tool, "query": user_query}, {"status": "success"})

        # Return a mock result for now
        return {
            "knowledge_graph": knowledge_graph,
            "web_search_results": web_search_results,
            "selected_tool": selected_tool,
        }