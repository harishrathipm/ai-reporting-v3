import logging
import smtplib
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class ActionDispatcherTool:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def dispatch(self, data, method, target):
        """
        Dispatches data to a specified target using the given method.

        Args:
            data (dict): The data to dispatch.
            method (str): The dispatch method (e.g., 'email', 'webhook').
            target (str): The target address or endpoint.

        Returns:
            dict: The result of the dispatch operation.
        """
        try:
            if method == 'email':
                return self._send_email(data, target)
            elif method == 'webhook':
                return self._send_webhook(data, target)
            else:
                raise ValueError(f"Unsupported dispatch method: {method}")
        except Exception as e:
            self.logger.error(f"Error dispatching data: {e}")
            return {'status': 'error', 'message': str(e)}

    def _send_email(self, data, email_address):
        """
        Sends data via email.

        Args:
            data (dict): The data to send.
            email_address (str): The recipient's email address.

        Returns:
            dict: The result of the email dispatch.
        """
        try:
            smtp_server = "smtp.example.com"
            smtp_port = 587
            sender_email = "noreply@example.com"
            sender_password = "password"

            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = email_address
            message['Subject'] = "Data Dispatch"
            message.attach(MIMEText(str(data), 'plain'))

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, email_address, message.as_string())

            self.logger.info(f"Email sent to {email_address} with data: {data}")
            return {'status': 'success', 'message': f"Email sent to {email_address}"}
        except Exception as e:
            self.logger.error(f"Error sending email: {e}")
            return {'status': 'error', 'message': str(e)}

    def _send_webhook(self, data, webhook_url):
        """
        Sends data to a webhook endpoint.

        Args:
            data (dict): The data to send.
            webhook_url (str): The webhook URL.

        Returns:
            dict: The result of the webhook dispatch.
        """
        try:
            response = requests.post(webhook_url, json=data)
            response.raise_for_status()
            self.logger.info(f"Data sent to webhook {webhook_url} with payload: {data}")
            return {'status': 'success', 'message': f"Data sent to webhook {webhook_url}"}
        except requests.RequestException as e:
            self.logger.error(f"Error sending webhook: {e}")
            return {'status': 'error', 'message': str(e)}