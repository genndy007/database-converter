import psycopg2
from app.db.config import POSTGRES_CONNECTION_DATA


class Postgres:
    def __enter__(self):
        self.conn = psycopg2.connect(**POSTGRES_CONNECTION_DATA)
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()
