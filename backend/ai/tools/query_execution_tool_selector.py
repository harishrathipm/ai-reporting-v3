class QueryExecutionToolSelector:
    def select_tool(self, step):
        """
        Selects the appropriate tool for executing a query step, considering execution constraints.

        Args:
            step (dict): A single step from the logical plan.

        Returns:
            str: The name of the tool to use (e.g., 'SQLTool', 'MongoTool').
        """
        db_type = step.get('db_type')
        constraints = step.get('constraints', {})

        if db_type == 'sql':
            if constraints.get('use_read_replica'):
                return 'SQLReadReplicaTool'
            return 'SQLTool'
        elif db_type == 'nosql':
            return 'MongoTool'
        elif db_type == 'csv':
            return 'CSVTool'
        elif db_type == 'graphql':
            return 'GraphQLTool'
        elif db_type == 'rest':
            return 'RESTTool'
        else:
            raise ValueError(f"Unsupported db_type: {db_type}. Supported types are: sql, nosql, csv, graphql, rest.")