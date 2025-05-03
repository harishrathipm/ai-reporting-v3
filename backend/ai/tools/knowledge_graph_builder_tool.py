import requests

class KnowledgeGraphBuilderTool:
    def __init__(self):
        """
        Initializes the KnowledgeGraphBuilderTool for building reusable knowledge graphs.
        """
        self.graph = {}

    def build_graph(self, schema):
        """
        Builds a knowledge graph from the provided schema.

        Args:
            schema (dict): The database schema containing tables and columns.

        Returns:
            dict: A knowledge graph representation of the schema.
        """
        for table, columns in schema.items():
            self.graph[table] = {
                "columns": columns,
                "relationships": []  # Placeholder for relationships
            }

        return self.graph

    def add_relationship(self, table1, table2, relationship):
        """
        Adds a relationship between two tables in the knowledge graph.

        Args:
            table1 (str): The name of the first table.
            table2 (str): The name of the second table.
            relationship (str): The type of relationship (e.g., "one-to-many").
        """
        if table1 in self.graph and table2 in self.graph:
            self.graph[table1]["relationships"].append({"table": table2, "type": relationship})
            self.graph[table2]["relationships"].append({"table": table1, "type": relationship})

    def get_graph(self):
        """
        Retrieves the current knowledge graph.

        Returns:
            dict: The knowledge graph.
        """
        return self.graph

class TavilyWebSearchTool:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.tavily.com/search"

    def search(self, query):
        """
        Perform a web search using Tavily.

        Args:
            query (str): The search query.

        Returns:
            dict: The search results.
        """
        headers = {"Authorization": f"Bearer {self.api_key}"}
        params = {"q": query}
        response = requests.get(self.base_url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()