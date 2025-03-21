import os

from dotenv import load_dotenv
from rococo.data.postgresql import PostgreSQLAdapter

load_dotenv()


def run():
    with open(os.path.join(os.path.dirname(__file__), "schema.sql"), "r") as file:
        query = file.read()

    db_adapter = PostgreSQLAdapter(
        host=os.environ.get("DB_HOST", "localhost"),
        port=int(os.environ.get("DB_PORT", "5432")),
        database=os.environ.get("DB_NAME", "rococo"),
        user=os.environ.get("DB_USER", "postgres"),
        password=os.environ.get("DB_PASSWORD", "postgres"),
    )

    with db_adapter:
        db_response = db_adapter.execute_query(query, {})
        result = db_adapter.parse_db_response(db_response)
        db_adapter._connection.commit()
        return result


if __name__ == "__main__":
    run()
