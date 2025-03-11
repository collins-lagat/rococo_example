import os
from typing import Type

from rococo.data import PostgreSQLAdapter
from rococo.repositories import BaseRepository


class RepositoryFactory:
    _repositories = {}

    @classmethod
    def _get_db_connection(cls):
        return PostgreSQLAdapter(
            host=os.environ.get("DB_HOST", "localhost"),
            port=int(os.environ.get("DB_PORT", "5432")),
            database=os.environ.get("DB_NAME", "rococo"),
            user=os.environ.get("DB_USER", "postgres"),
            password=os.environ.get("DB_PASSWORD", "postgres"),
        )

    @classmethod
    def _get_message_adapter(self):
        return None

    @classmethod
    def get_repository(cls, repo_class: Type[BaseRepository]) -> BaseRepository:
        if repo_class not in cls._repositories:
            adapter = cls._get_db_connection()
            message_adapter = cls._get_message_adapter()
            cls._repositories[repo_class] = repo_class(
                adapter, message_adapter=message_adapter
            )
        return cls._repositories[repo_class]
