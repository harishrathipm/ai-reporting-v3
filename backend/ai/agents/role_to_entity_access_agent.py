from app.utils.llm import LLM

class RoleToEntityAccessAgent:
    def __init__(self):
        self.llm = LLM()

    def get_accessible_entities(self, role):
        """
        Determines the entities or tables a user can access based on their role.

        Args:
            role (str): The role of the user (e.g., 'Executive', 'Analyst').

        Returns:
            list: A list of accessible entities or tables.
        """
        predefined_roles = {
            'Executive': ['table1', 'table2', 'table3'],
            'Analyst': ['table1', 'table2']
        }

        if role not in predefined_roles:
            raise ValueError(f"Invalid role: {role}. Allowed roles are: {list(predefined_roles.keys())}")

        return predefined_roles[role]