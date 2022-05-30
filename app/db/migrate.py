from app.db.sqlite import SQLite
from app.db.postgres import Postgres
from app.db.mysql import MySQL
from app.db import TABLE_NAMES
from app.db.config import DB_NAME, MYSQL_TABLE_FIELDS


def migrate_sqlite_to_pg():
    with SQLite() as sqlite_cur, Postgres() as pg_cur:
        for table_name in TABLE_NAMES:
            rows = sqlite_cur.execute(f'SELECT * FROM {table_name}').fetchall()
            for row in rows:
                pg_cur.execute(f'INSERT INTO {table_name} VALUES {row}')


# only 3 fields from pg, 3 entries to change
def migrate_pg_to_mysql():
    with Postgres() as pg_cur, MySQL() as my_cur:
        my_cur.execute(f'use {DB_NAME}')
        for table_name in TABLE_NAMES:
            fields = ', '.join(MYSQL_TABLE_FIELDS[table_name])
            pg_cur.execute(f'SELECT {fields} FROM {table_name}')
            rows = pg_cur.fetchall()
            for row in rows:
                my_cur.execute(f'INSERT INTO {table_name}({fields}) VALUES {row}')

        # update rows
        for pk in (1, 2, 3):
            my_cur.execute(f'''update customers set address = concat('updated ', address) where customer_id = {pk}''')
            my_cur.execute(f'''update suppliers set company_name = concat('updated ', company_name) where supplier_id = {pk}''')
            my_cur.execute(f'''update hardwares set item_name = concat('updated ', item_name) where hardware_id = {pk}''')

        my_cur.execute('select * from customers')
        print(my_cur.fetchall())
        my_cur.close()
