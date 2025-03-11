from rococo.data.postgresql import PostgreSQLAdapter
from rococo.messaging.base import MessageAdapter
from rococo.models import Organization
from rococo.repositories.postgresql import PostgreSQLRepository


class OrganizationRepository(PostgreSQLRepository):
    def __init__(
        self,
        adapter: PostgreSQLAdapter,
        message_adapter: MessageAdapter,
    ):
        super().__init__(adapter, Organization, message_adapter, "organization")
