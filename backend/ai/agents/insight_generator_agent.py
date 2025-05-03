from app.utils.llm import LLM

class InsightGeneratorAgent:
    def __init__(self):
        self.llm = LLM()

    def generate_insights(self, query_result, user_query):
        """
        Generates insights from the query result and user query.

        Args:
            query_result (list): The result of the executed query.
            user_query (str): The original user query.

        Returns:
            str: A summary of insights generated from the query result.
        """
        prompt = (
            "Given the following query result and user query, generate a summary of insights, including statistical analyses like correlations, trends, and actionable recommendations.\n"
            f"Query Result: {query_result}\n"
            f"User Query: {user_query}"
        )
        insights = self.llm.generate_response(prompt)

        return insights