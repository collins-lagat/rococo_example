import os

from dotenv import load_dotenv
from rococo.data.postgresql import PostgreSQLAdapter

load_dotenv()

query = """
    DROP TABLE IF EXISTS public.organization;
    DROP TABLE IF EXISTS public.organization_audit;
    DROP TABLE IF EXISTS public.person;
    DROP TABLE IF EXISTS public.person_audit;
    DROP TABLE IF EXISTS public.email;
    DROP TABLE IF EXISTS public.email_audit;
    DROP TABLE IF EXISTS public.person_organization_role;
    DROP TABLE IF EXISTS public.person_organization_role_audit;
    DROP TABLE IF EXISTS public.otp_method;
    DROP TABLE IF EXISTS public.otp_method_audit;
    DROP TABLE IF EXISTS public.recovery_code;
    DROP TABLE IF EXISTS public.recovery_code_audit;
    DROP TABLE IF EXISTS public.login_method;
    DROP TABLE IF EXISTS public.login_method_audit;
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
