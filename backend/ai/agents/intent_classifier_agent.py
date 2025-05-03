from app.utils.llm import LLM

class IntentClassifierAgent:
    def __init__(self):
        """
        Initializes the IntentClassifierAgent for session management.
        """
        self.llm = LLM()

    def classify_intent(self, user_message, session_context):
        """
        Classifies the user's intent based on the message and session context.

        Args:
            user_message (str): The user's message.
            session_context (dict): The current session context.

        Returns:
            str: The classified intent (e.g., "new_session", "clarification").
        """
        prompt = (
            "Given the following user message and session context, classify the intent as either 'new_session' or 'clarification'.\n"
            f"User Message: {user_message}\n"
            f"Session Context: {session_context}"
        )
        return self.llm.generate_response(prompt).strip()