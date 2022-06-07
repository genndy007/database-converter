import os
import sqlite3
from app.db import SQL_DIR, CACHE_DIR

DB_INIT_SCRIPT = 'init_hw_lite.sql'
DB_FILE_NAME = 'hw_storage.sqlite3'


class SQLite:
    def __init__(self, file=f'{CACHE_DIR}/{DB_FILE_NAME}'):
        self.file = file

    def __enter__(self):
        self.conn = sqlite3.connect(self.file)
        # self.conn.row_factory = sqlite3.Row
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()


def init_hw_sqlite_db(file_name=DB_FILE_NAME):
    os.remove(f'{CACHE_DIR}/{file_name}')
    with SQLite() as cur:
        with open(f'{SQL_DIR}/{DB_INIT_SCRIPT}') as sql:
            cur.executescript(sql.read())
