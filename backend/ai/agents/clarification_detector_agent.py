from app.utils.llm import LLM

class ClarificationDetectorAgent:
    def __init__(self):
        """
        Initializes the ClarificationDetectorAgent for detecting query clarifications.
        """
        self.llm = LLM()

    def detect_clarification(self, user_message, previous_query):
        """
        Detects if the user's message is a clarification of the previous query.

        Args:
            user_message (str): The user's message.
            previous_query (str): The previous query from the user.

        Returns:
            bool: True if the message is a clarification, False otherwise.
        """
        prompt = (
            "Given the following user message and previous query, determine if the message is a clarification of the query.\n"
            f"User Message: {user_message}\n"
            f"Previous Query: {previous_query}"
        )
        response = self.llm.generate_response(prompt).strip().lower()
        return response == "yes"