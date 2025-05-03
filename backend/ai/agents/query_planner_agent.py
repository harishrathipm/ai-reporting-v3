from app.utils.llm import LLM
from tools.db_introspector_tool import DBIntrospectorTool
from agents.semantic_enricher_agent import SemanticEnricherAgent

class QueryPlannerAgent:
    def __init__(self):
        self.llm = LLM()
        self.db_introspector = DBIntrospectorTool()
        self.semantic_enricher = SemanticEnricherAgent()

    def plan_query(self, user_query, db_connection, user_feedback=None):
        """
        Converts a user query into a logical plan, incorporating user feedback if provided.

        Args:
            user_query (str): The natural language query from the user.
            db_connection: The database connection object.
            user_feedback (str, optional): Feedback from the user to refine the plan.

        Returns:
            dict: A logical plan containing steps for query execution.
        """
        # Step 1: Introspect the database schema
        schema = self.db_introspector.introspect_schema(db_connection)

        # Step 2: Enrich the schema semantically
        enriched_schema = self.semantic_enricher.enrich_schema(schema)

        # Step 3: Generate a logical plan using the LLM
        prompt = (
            "Given the following database schema and user query, generate a logical plan for execution.\n"
            f"Schema: {enriched_schema}\n"
            f"Query: {user_query}\n"
        )

        if user_feedback:
            prompt += f"User Feedback: {user_feedback}\n"

        logical_plan = self.llm.generate_response(prompt)

        return logical_plan