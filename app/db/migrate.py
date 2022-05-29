from app.db.sqlite import SQLite
from app.db.postgres import Postgres
from app.db import TABLE_NAMES


def migrate_sqlite_to_pg():
    with SQLite() as sqlite_cur, Postgres() as pg_cur:
        for table_name in TABLE_NAMES:
            rows = sqlite_cur.execute(f'SELECT * FROM {table_name}').fetchall()
            for row in rows:
                pg_cur.execute(f'INSERT INTO {table_name} VALUES {row}')

