import mysql.connector
from app.db.config import MYSQL_CONNECTION_DATA
from app.db.config import DB_NAME
from app.db import SQL_DIR

DB_INIT_SCRIPT = 'init_hw_my.sql'


class MySQL:
    def __enter__(self):
        self.conn = mysql.connector.connect(**MYSQL_CONNECTION_DATA)
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()


def recreate_mysql_db():
    with MySQL() as cur:
        cur.execute(f'drop database if exists {DB_NAME}')
        cur.execute(f'create database {DB_NAME}')


def init_hw_mysql_db():
    with MySQL() as cur:
        cur.execute(f'use {DB_NAME}')
        with open(f'{SQL_DIR}/{DB_INIT_SCRIPT}') as sql:
            cur.execute(sql.read(), multi=True)
