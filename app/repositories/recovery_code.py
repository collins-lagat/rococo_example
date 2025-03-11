from rococo.data.postgresql import PostgreSQLAdapter
from rococo.messaging.base import MessageAdapter
from rococo.models.recovery_code import RecoveryCode
from rococo.repositories.postgresql import PostgreSQLRepository


class RecoveryCodeRepository(PostgreSQLRepository):
    def __init__(self, adapter: PostgreSQLAdapter, message_adapter: MessageAdapter):
        super().__init__(adapter, RecoveryCode, message_adapter, "recovery_code")
