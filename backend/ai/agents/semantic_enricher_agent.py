from app.utils.llm import LLM

class SemanticEnricherAgent:
    def __init__(self):
        self.llm = LLM()

    def enrich_schema(self, schema):
        """
        Enriches the database schema with semantic information using an LLM.

        Args:
            schema (dict): The raw database schema.

        Returns:
            dict: The enriched schema with semantic annotations.
        """
        prompt = (
            "Given the following database schema, provide semantic annotations for each table and column.\n"
            f"Schema: {schema}"
        )
        enriched_schema = self.llm.generate_response(prompt)

        return enriched_schema