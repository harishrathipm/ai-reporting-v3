from pymongo import MongoClient

class TempStorage:
    def __init__(self, mongo_uri, db_name):
        """
        Initializes the TempStorage for temporary data storage.

        Args:
            mongo_uri (str): The MongoDB connection URI.
            db_name (str): The name of the database to use.
        """
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.temp_data = self.db["temp_data"]

        # Ensure indexes for faster queries and TTL for automatic cleanup
        self.temp_data.create_index("session_id")
        self.temp_data.create_index("step_id")
        self.temp_data.create_index("timestamp", expireAfterSeconds=86400)  # 1 day TTL

    def store_data(self, session_id, step_id, data):
        """
        Stores temporary data for a specific session and step.

        Args:
            session_id (str): The ID of the session.
            step_id (str): The ID of the step.
            data (dict): The data to store.
        """
        temp_entry = {
            "session_id": session_id,
            "step_id": step_id,
            "data": data
        }
        self.temp_data.insert_one(temp_entry)

    def retrieve_data(self, session_id, step_id):
        """
        Retrieves temporary data for a specific session and step.

        Args:
            session_id (str): The ID of the session.
            step_id (str): The ID of the step.

        Returns:
            dict: The retrieved data.
        """
        return self.temp_data.find_one({"session_id": session_id, "step_id": step_id})

    def delete_data(self, session_id):
        """
        Deletes all temporary data for a given session.

        Args:
            session_id (str): The ID of the session.
        """
        self.temp_data.delete_many({"session_id": session_id})