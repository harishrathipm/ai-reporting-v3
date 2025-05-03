import re

class ExecutionGuardrails:
    @staticmethod
    def log_validation_failure(query, reason):
        """
        Logs the reason for query validation failure.

        Args:
            query (str): The query that failed validation.
            reason (str): The reason for the failure.
        """
        print(f"Validation failed for query: {query}. Reason: {reason}")

    @staticmethod
    def validate_query(query, custom_rules=None):
        """
        Validates a query for SQL injection patterns, unsafe complexity, and custom rules.

        Args:
            query (str): The query to validate.
            custom_rules (list, optional): Additional regex patterns for validation.

        Returns:
            bool: True if the query is safe, False otherwise.
        """
        # Default SQL injection patterns
        sql_injection_patterns = [
            r"(--|;|\bOR\b|\bAND\b).*\b(SELECT|INSERT|UPDATE|DELETE)\b",
            r"\bUNION\b.*\bSELECT\b",
            r"\bDROP\b.*\bTABLE\b",
            r"\bEXEC\b.*\bSP_",
            r"\bINSERT\b.*\bINTO\b",
            r"\bDELETE\b.*\bFROM\b",
            r"\bUPDATE\b.*\bSET\b",
        ]

        # Include custom rules if provided
        if custom_rules:
            sql_injection_patterns.extend(custom_rules)

        for pattern in sql_injection_patterns:
            if re.search(pattern, query, re.IGNORECASE):
                ExecutionGuardrails.log_validation_failure(query, f"Matched pattern: {pattern}")
                return False

        # Check for excessive query complexity
        if query.lower().count("join") > 5:
            ExecutionGuardrails.log_validation_failure(query, "Too many JOINs")
            return False
        if query.lower().count("select") > 3:  # Too many nested SELECTs
            ExecutionGuardrails.log_validation_failure(query, "Too many nested SELECTs")
            return False

        return True

    @staticmethod
    def enforce_row_limit(query, limit=1000):
        """
        Enforces a row limit on the query if not already present.

        Args:
            query (str): The query to modify.
            limit (int): The maximum number of rows to return.

        Returns:
            str: The modified query with a row limit.
        """
        if "limit" not in query.lower():
            return f"{query.strip()} LIMIT {limit}"
        return query

    @staticmethod
    def sanitize_query(query):
        """
        Sanitizes a query by removing potentially harmful characters.

        Args:
            query (str): The query to sanitize.

        Returns:
            str: The sanitized query.
        """
        # Remove semicolons and comments
        sanitized_query = re.sub(r"(--|;|#).*", "", query)
        return sanitized_query.strip()