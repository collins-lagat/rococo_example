import smtplib
from typing import Any


class SMTPService:
    def __init__(
        self,
        host=None,
        port=None,
        username=None,
        password=None,
    ):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.connection = None

    def open(self):
        try:
            self.connection = smtplib.SMTP(self.host, self.port)
            self.connection.login(self.username, self.password)
            return True
        except Exception as e:
            raise e

    def close(self):
        try:
            try:
                self.connection.quit()
            except smtplib.SMTPException as e:
                raise e
        finally:
            self.connection = None

    def send_email(self, message: dict) -> Any:
        self.open()
        try:
            self.connection.sendmail(
                message["from"],
                message["to"],
                message["message"],
            )
        except Exception as e:
            raise e
        finally:
            self.close()
