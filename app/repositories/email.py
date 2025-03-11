from rococo.data.postgresql import PostgreSQLAdapter
from rococo.messaging.base import MessageAdapter
from rococo.models.email import Email
from rococo.repositories.postgresql import PostgreSQLRepository


class EmailRepository(PostgreSQLRepository):
    def __init__(self, adapter: PostgreSQLAdapter, message_adapter: MessageAdapter):
        super().__init__(adapter, Email, message_adapter, "email")
