import psycopg2
from app.db.config import POSTGRES_CONNECTION_DATA
from app.db import SQL_DIR

DB_INIT_SCRIPT = 'init_hw_postgre.sql'

class Postgres:
    def __enter__(self):
        self.conn = psycopg2.connect(**POSTGRES_CONNECTION_DATA)
        self.conn.autocommit = True
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

def init_hw_pg_db():
    with Postgres() as cur:
        with open(f'{SQL_DIR}/{DB_INIT_SCRIPT}') as sql:
            cur.execute(sql.read())
