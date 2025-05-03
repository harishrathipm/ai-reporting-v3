import logging
from pymongo import MongoClient

class ResultMetadataTracker:
    def __init__(self, mongo_uri="mongodb://localhost:27017", db_name="metadata_db"):
        self.metadata = []
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.collection = self.db["metadata"]

    def log_step_metadata(self, step, result):
        """
        Logs metadata for a single query execution step.

        Args:
            step (dict): The step details from the logical plan.
            result (dict): The result of the step execution.
        """
        metadata_entry = {
            'step_id': step.get('step_id'),
            'tool': step.get('tool'),
            'query': step.get('query'),
            'status': result.get('status'),
            'runtime': result.get('runtime', 'N/A'),
            'output': result.get('data', 'N/A'),
            'memory_usage': result.get('memory_usage', 'N/A'),
            'error_details': result.get('error_details', 'None'),
            'timestamp': result.get('timestamp', 'N/A')
        }
        self.metadata.append(metadata_entry)
        self.collection.insert_one(metadata_entry)
        logging.info(f"Logged metadata for step: {metadata_entry}")

    def get_metadata(self, step_id=None, limit=100):
        """
        Retrieves logged metadata with optional filtering and limits.

        Args:
            step_id (str, optional): The step ID to filter metadata. Defaults to None.
            limit (int, optional): The maximum number of entries to retrieve. Defaults to 100.

        Returns:
            list: A list of metadata entries.
        """
        query = {"step_id": step_id} if step_id else {}
        return list(self.collection.find(query).limit(limit))