import os

from dotenv import load_dotenv
from rococo.data.postgresql import PostgreSQLAdapter

load_dotenv()

query = """
    TRUNCATE TABLE public.organization;
    TRUNCATE TABLE public.organization_audit;
    TRUNCATE TABLE public.person;
    TRUNCATE TABLE public.person_audit;
    TRUNCATE TABLE public.email;
    TRUNCATE TABLE public.email_audit;
    TRUNCATE TABLE public.person_organization_role;
    TRUNCATE TABLE public.person_organization_role_audit;
    TRUNCATE TABLE public.otp_method;
    TRUNCATE TABLE public.otp_method_audit;
    TRUNCATE TABLE public.recovery_code;
    TRUNCATE TABLE public.recovery_code_audit;
    TRUNCATE TABLE public.login_method;
    TRUNCATE TABLE public.login_method_audit;
"""


def run():
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
