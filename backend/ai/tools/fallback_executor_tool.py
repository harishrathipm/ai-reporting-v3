import logging
from query_execution_tool_selector import QueryExecutionToolSelector
from query_executor_tool import QueryExecutorTool

class FallbackExecutorTool:
    def __init__(self):
        self.tool_selector = QueryExecutionToolSelector()
        self.executor = QueryExecutorTool()
        self.logger = logging.getLogger(__name__)

    def execute_with_fallback(self, step, db_connection):
        """
        Executes a query step with fallback mechanisms.

        Args:
            step (dict): A single step from the logical plan.
            db_connection: The database connection object.

        Returns:
            dict: The result of the query execution.
        """
        try:
            # Attempt to execute the step
            result = self.executor.execute_step(step, db_connection)

            # If execution is successful, return the result
            if result['status'] == 'success':
                self.logger.info(f"Step {step['step_id']} executed successfully with tool {step['tool']}.")
                return result

            # Log the failure and attempt fallback
            self.logger.warning(f"Primary execution failed for step {step['step_id']} with tool {step['tool']}. Attempting fallback.")
            return self._attempt_fallback(step, db_connection)

        except Exception as e:
            self.logger.error(f"Error during execution with fallback for step {step['step_id']}: {e}")
            return {'status': 'error', 'message': str(e)}

    def _attempt_fallback(self, step, db_connection):
        """
        Attempts to execute the step using an alternate tool or strategy.

        Args:
            step (dict): A single step from the logical plan.
            db_connection: The database connection object.

        Returns:
            dict: The result of the fallback execution.
        """
        try:
            # Modify the step to use an alternate tool
            alternate_tool = self.tool_selector.select_tool(step)
            self.logger.info(f"Selected alternate tool {alternate_tool} for step {step['step_id']}.")
            step['tool'] = alternate_tool

            # Re-execute the step with the alternate tool
            result = self.executor.execute_step(step, db_connection)

            if result['status'] == 'success':
                self.logger.info(f"Fallback execution succeeded for step {step['step_id']} with tool {alternate_tool}.")
            else:
                self.logger.warning(f"Fallback execution failed for step {step['step_id']} with tool {alternate_tool}.")

            return result

        except Exception as e:
            self.logger.error(f"Fallback execution failed for step {step['step_id']} with error: {e}")
            return {'status': 'error', 'message': f"Fallback failed: {str(e)}"}