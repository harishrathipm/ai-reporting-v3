class VisualizationBuilderModel:
    def build_visualization(self, query_result, chart_type):
        """
        Builds a visualization configuration from the query result.

        Args:
            query_result (list): The result of the executed query.
            chart_type (str): The type of chart to generate (e.g., 'bar', 'line', 'pie', 'scatter', 'heatmap').

        Returns:
            dict: A configuration for rendering the chart.
        """
        if chart_type == 'bar':
            return {
                'type': 'bar',
                'data': {
                    'labels': [row[0] for row in query_result],
                    'datasets': [
                        {
                            'label': 'Values',
                            'data': [row[1] for row in query_result],
                            'backgroundColor': 'rgba(75, 192, 192, 0.2)',
                            'borderColor': 'rgba(75, 192, 192, 1)',
                            'borderWidth': 1,
                        }
                    ],
                },
                'options': {
                    'responsive': True,
                    'scales': {
                        'y': {
                            'beginAtZero': True,
                        },
                    },
                },
            }
        elif chart_type == 'line':
            return {
                'type': 'line',
                'data': {
                    'labels': [row[0] for row in query_result],
                    'datasets': [
                        {
                            'label': 'Values',
                            'data': [row[1] for row in query_result],
                            'fill': False,
                            'borderColor': 'rgba(75, 192, 192, 1)',
                            'tension': 0.1,
                        }
                    ],
                },
                'options': {
                    'responsive': True,
                    'scales': {
                        'y': {
                            'beginAtZero': True,
                        },
                    },
                },
            }
        elif chart_type == 'pie':
            return {
                'type': 'pie',
                'data': {
                    'labels': [row[0] for row in query_result],
                    'datasets': [
                        {
                            'data': [row[1] for row in query_result],
                            'backgroundColor': [
                                'rgba(255, 99, 132, 0.2)',
                                'rgba(54, 162, 235, 0.2)',
                                'rgba(255, 206, 86, 0.2)',
                            ],
                            'borderColor': [
                                'rgba(255, 99, 132, 1)',
                                'rgba(54, 162, 235, 1)',
                                'rgba(255, 206, 86, 1)',
                            ],
                            'borderWidth': 1,
                        }
                    ],
                },
                'options': {
                    'responsive': True,
                },
            }
        elif chart_type == 'scatter':
            return {
                'type': 'scatter',
                'data': {
                    'datasets': [
                        {
                            'label': 'Scatter Dataset',
                            'data': [{'x': row[0], 'y': row[1]} for row in query_result],
                            'backgroundColor': 'rgba(75, 192, 192, 0.2)',
                            'borderColor': 'rgba(75, 192, 192, 1)',
                        }
                    ],
                },
                'options': {
                    'responsive': True,
                },
            }
        elif chart_type == 'heatmap':
            return {
                'type': 'heatmap',
                'data': {
                    'labels': [row[0] for row in query_result],
                    'datasets': [
                        {
                            'data': [row[1] for row in query_result],
                            'backgroundColor': 'rgba(255, 99, 132, 0.2)',
                        }
                    ],
                },
                'options': {
                    'responsive': True,
                },
            }
        else:
            raise ValueError(f"Unsupported chart type: {chart_type}. Supported types are: bar, line, pie, scatter, heatmap.")