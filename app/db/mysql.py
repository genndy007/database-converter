import mysql.connector
from app.db.config import MYSQL_CONNECTION_DATA
from app.db.config import DB_NAME

class MySQL:
    def __enter__(self):
        self.conn = mysql.connector.connect(**MYSQL_CONNECTION_DATA)
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()


def recreate_mysql_db():
    with MySQL() as cur:
        cur.execute(f'drop database if exists {DB_NAME}')
        cur.execute(f'create database {DB_NAME}')


def init_hw_mysql_db():
    with MySQL() as cur:
        pass