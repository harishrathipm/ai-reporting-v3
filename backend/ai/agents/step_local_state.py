from pymongo import MongoClient
from datetime import datetime

class StepLocalState:
    def __init__(self, mongo_uri, db_name):
        """
        Initializes the StepLocalState for session step tracking.

        Args:
            mongo_uri (str): The MongoDB connection URI.
            db_name (str): The name of the database to use.
        """
        self.mongo_client = MongoClient(mongo_uri)
        self.db = self.mongo_client[db_name]
        self.session_steps = self.db["session_steps"]
        self.step_states = self.db["step_states"]

        # Ensure indexes for faster queries and TTL for automatic cleanup
        self.session_steps.create_index("session_id")
        self.step_states.create_index("session_id")
        self.step_states.create_index("step_id")
        self.step_states.create_index("timestamp", expireAfterSeconds=604800)  # 7 days TTL

    def log_step(self, session_id, step_data):
        """
        Logs a step's data into the session_steps collection.

        Args:
            session_id (str): The ID of the session.
            step_data (dict): The data to log for the step.
        """
        step_data["session_id"] = session_id
        self.session_steps.insert_one(step_data)

    def get_steps(self, session_id):
        """
        Retrieves all steps for a given session.

        Args:
            session_id (str): The ID of the session.

        Returns:
            list: A list of steps for the session.
        """
        return list(self.session_steps.find({"session_id": session_id}))

    def delete_steps(self, session_id):
        """
        Deletes all steps for a given session.

        Args:
            session_id (str): The ID of the session.
        """
        self.session_steps.delete_many({"session_id": session_id})

    def store_step_state(self, session_id, step_id, state):
        """
        Store the state of a specific step.

        Args:
            session_id (str): The ID of the session.
            step_id (str): The ID of the step.
            state (dict): The state data to store.
        """
        self.step_states.insert_one({
            "session_id": session_id,
            "step_id": step_id,
            "state": state,
            "timestamp": datetime.utcnow()
        })

    def get_step_state(self, session_id, step_id):
        """
        Retrieve the state of a specific step.

        Args:
            session_id (str): The ID of the session.
            step_id (str): The ID of the step.

        Returns:
            dict: The state data of the step.
        """
        return self.step_states.find_one({"session_id": session_id, "step_id": step_id})