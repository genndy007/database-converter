from app.db.sqlite import SQLite
from app.db.postgres import Postgres
from app.db.mysql import MySQL
from app.db import TABLE_NAMES
from app.db.config import DB_NAME


def migrate_sqlite_to_pg():
    with SQLite() as sqlite_cur, Postgres() as pg_cur:
        for table_name in TABLE_NAMES:
            rows = sqlite_cur.execute(f'SELECT * FROM {table_name}').fetchall()
            for row in rows:
                pg_cur.execute(f'INSERT INTO {table_name} VALUES {row}')


def migrate_pg_to_mysql():
    with Postgres() as pg_cur, MySQL() as my_cur:
        my_cur.execute(f'use {DB_NAME}')
        for table_name in TABLE_NAMES:
            pg_cur.execute(f'SELECT * FROM {table_name}')
            rows = pg_cur.fetchall()
            for row in rows:
                my_cur.execute(f'INSERT INTO {table_name} VALUES {row}')

        my_cur.close()
