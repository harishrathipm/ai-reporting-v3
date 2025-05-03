from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import logging
import csv

class QueryExecutorTool:
    def execute_step(self, step, db_connection):
        """
        Executes a single query step with safety checks.

        Args:
            step (dict): A single step from the logical plan.
            db_connection: The database connection string or object.

        Returns:
            dict: The result of the query execution.
        """
        try:
            query = step.get('query')
            tool = step.get('tool')

            if tool == 'SQLTool':
                # Execute SQL query using SQLAlchemy
                engine = create_engine(db_connection)
                with engine.connect() as connection:
                    result = connection.execute(query).fetchall()
            elif tool == 'MongoTool':
                # Execute MongoDB query
                result = db_connection[step['target_table']].find(query)
            elif tool == 'CSVTool':
                # Execute CSV query (e.g., filter rows)
                result = self.execute_csv_query(step, db_connection)
            else:
                raise ValueError(f"Unsupported tool: {tool}")

            return {'status': 'success', 'data': result}
        except SQLAlchemyError as e:
            logging.error(f"SQLAlchemy error executing step: {e}")
            return {'status': 'error', 'message': str(e)}
        except Exception as e:
            logging.error(f"Error executing step: {e}")
            return {'status': 'error', 'message': str(e)}

    def execute_csv_query(self, step, db_connection):
        """
        Executes a query on a CSV file.

        Args:
            step (dict): A single step from the logical plan.
            db_connection: The CSV file path or handler.

        Returns:
            list: Filtered rows from the CSV file.
        """
        results = []
        with open(db_connection, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Replace unsafe eval with a safe parser
                if self.safe_csv_filter(row, step['query']):
                    results.append(row)

        return results

    def safe_csv_filter(self, row, query):
        """
        Safely filters a row based on the query.

        Args:
            row (dict): A single row from the CSV file.
            query (str): The query string to evaluate.

        Returns:
            bool: True if the row matches the query, False otherwise.
        """
        # Implement a safe query parser here
        # For now, return True as a placeholder
        return True