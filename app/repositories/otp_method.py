from rococo.data.postgresql import PostgreSQLAdapter
from rococo.messaging.base import MessageAdapter
from rococo.models.otp_method import OtpMethod
from rococo.repositories.postgresql import PostgreSQLRepository


class OtpMethodRepository(PostgreSQLRepository):
    def __init__(self, adapter: PostgreSQLAdapter, message_adapter: MessageAdapter):
        super().__init__(adapter, OtpMethod, message_adapter, "otp_method")
