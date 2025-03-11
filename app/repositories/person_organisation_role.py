from rococo.data.postgresql import PostgreSQLAdapter
from rococo.messaging.base import MessageAdapter
from rococo.models.person_organization_role import PersonOrganizationRole
from rococo.repositories.postgresql import PostgreSQLRepository


class PersonOrganizationRoleRepository(PostgreSQLRepository):
    def __init__(self, adapter: PostgreSQLAdapter, message_adapter: MessageAdapter):
        super().__init__(
            adapter, PersonOrganizationRole, message_adapter, "person_organization_role"
        )
