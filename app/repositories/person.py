from rococo.data.postgresql import PostgreSQLAdapter
from rococo.messaging.base import MessageAdapter
from rococo.models.person import Person
from rococo.repositories.postgresql import PostgreSQLRepository


class PersonRepository(PostgreSQLRepository):
    def __init__(self, adapter: PostgreSQLAdapter, message_adapter: MessageAdapter):
        super().__init__(adapter, Person, message_adapter, "person")
