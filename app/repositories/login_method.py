from rococo.data.postgresql import PostgreSQLAdapter
from rococo.messaging.base import MessageAdapter
from rococo.models.login_method import LoginMethod
from rococo.repositories.postgresql import PostgreSQLRepository


class LoginMethodRepository(PostgreSQLRepository):
    def __init__(self, adapter: PostgreSQLAdapter, message_adapter: MessageAdapter):
        super().__init__(adapter, LoginMethod, message_adapter, "login_method")
