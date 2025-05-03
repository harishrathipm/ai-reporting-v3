from app.utils.llm import LLM

class UserRoleResolverAgent:
    def __init__(self):
        self.llm = LLM()

    def resolve_role(self, user_query):
        """
        Resolves the role of the user based on the query.

        Args:
            user_query (str): The natural language query from the user.

        Returns:
            str: The resolved role (e.g., 'Executive', 'Analyst').
        """
        prompt = (
            "Given the following user query, determine the user's role. "
            "The roles are: 'Executive' or 'Analyst'.\n"
            f"Query: {user_query}"
        )
        role = self.llm.generate_response(prompt)
        return role.strip()