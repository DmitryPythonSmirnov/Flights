import psycopg2
from config import database, user, password, host, port


def get_conn():
    conn = psycopg2.connect(
        database=database,
        user=user,
        password=password,
        host=host,
        port=port
    )

    return conn
