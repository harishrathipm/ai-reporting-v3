from sqlalchemy import create_engine, inspect

class DBIntrospectorTool:
    def introspect_schema(self, db_connection):
        """
        Extracts the schema from the connected database.

        Args:
            db_connection (str): The database connection string.

        Returns:
            dict: A dictionary containing tables and their columns.
        """
        engine = create_engine(db_connection)
        inspector = inspect(engine)

        schema = {}
        for table_name in inspector.get_table_names():
            columns = inspector.get_columns(table_name)
            schema[table_name] = [column['name'] for column in columns]

        return schema