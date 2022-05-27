import sqlite3
from app.db import SQL_DIR, CACHE_DIR

DB_INIT_SCRIPT = 'init_hw.sql'

class SQLite:
    def __init__(self, file=f'{CACHE_DIR}/db.sqlite3'):
        self.file = file

    def __enter__(self):
        self.conn = sqlite3.connect(self.file)
        # self.conn.row_factory = sqlite3.Row
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()


def initialize_hw_database():
    with SQLite() as cur:
        with open(f'{SQL_DIR}/{DB_INIT_SCRIPT}') as sql:
            cur.executescript(sql.read())

        for row in cur.execute('select * from purchases'):
            print(row)