class ReactFormatterAgent:
    def format_for_react(self, data, response_type):
        """
        Formats data for rendering in React components.

        Args:
            data (dict): The data to format.
            response_type (str): The type of response (e.g., 'table', 'chart', 'text').

        Returns:
            dict: A formatted response suitable for React rendering.
        """
        if response_type == 'table':
            return {
                'type': 'table',
                'columns': data.get('columns', []),
                'rows': data.get('rows', []),
            }
        elif response_type == 'chart':
            return {
                'type': 'chart',
                'chartType': data.get('chartType', 'bar'),
                'data': data.get('data', {}),
                'options': data.get('options', {}),
            }
        elif response_type == 'text':
            return {
                'type': 'text',
                'data': {'response': data.get('response', '')},
            }
        elif response_type == 'error':
            return {
                'type': 'error',
                'message': data.get('message', 'An error occurred.'),
            }
        elif response_type == 'json':
            return {
                'type': 'json',
                'data': data,
            }
        elif response_type == 'xml':
            return {
                'type': 'xml',
                'data': data.get('xml', '<root></root>'),
            }
        else:
            return {
                'type': 'unsupported',
                'message': f"Unsupported response type: {response_type}. Supported types are: table, chart, text, error, json, xml.",
            }