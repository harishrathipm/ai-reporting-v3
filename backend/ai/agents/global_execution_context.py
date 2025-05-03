from pymongo import MongoClient
from datetime import datetime, timedelta

class GlobalExecutionContext:
    def __init__(self, mongo_uri, db_name):
        """
        Initializes the global execution context.

        Args:
            mongo_uri (str): The MongoDB connection URI.
            db_name (str): The name of the database to use.
        """
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.sessions = self.db["sessions"]
        self.metadata = self.db["metadata"]
        self.temp_results = self.db["temp_results"]  # Added for temporary query/intent results

    def create_session(self, user_id):
        """
        Creates a new session for a user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            dict: The created session document.
        """
        session = {
            "user_id": user_id,
            "state": {},
            "metadata": {},
            "results": [],
            "created_at": datetime.utcnow(),
            "expires_at": datetime.utcnow() + timedelta(hours=1)  # 1-hour TTL
        }
        self.sessions.insert_one(session)
        print(f"Session created for user {user_id} with TTL of 1 hour.")
        return session

    def update_session(self, session_id, updates):
        """
        Updates an existing session with new data.

        Args:
            session_id (str): The ID of the session to update.
            updates (dict): The updates to apply to the session.
        """
        self.sessions.update_one({"_id": session_id}, {"$set": updates})

    def get_session(self, session_id):
        """
        Retrieves a session by its ID.

        Args:
            session_id (str): The ID of the session to retrieve.

        Returns:
            dict: The session document.
        """
        return self.sessions.find_one({"_id": session_id})

    def delete_session(self, session_id):
        """
        Deletes a session by its ID.

        Args:
            session_id (str): The ID of the session to delete.
        """
        self.sessions.delete_one({"_id": session_id})
        print(f"Session {session_id} deleted.")

    def store_temp_result(self, session_id, step_id, result):
        """
        Store temporary query/intent result for a specific session and step.

        Args:
            session_id (str): The ID of the session.
            step_id (str): The ID of the step.
            result (dict): The result to store.
        """
        self.temp_results.insert_one({
            "session_id": session_id,
            "step_id": step_id,
            "result": result,
            "timestamp": datetime.utcnow()
        })

    def purge_temp_results(self, older_than_days):
        """
        Purge temporary results older than a specified number of days.

        Args:
            older_than_days (int): The number of days to retain results.
        """
        cutoff_date = datetime.utcnow() - timedelta(days=older_than_days)
        self.temp_results.delete_many({"timestamp": {"$lt": cutoff_date}})