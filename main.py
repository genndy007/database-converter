from app.db.postgres import Postgres


with Postgres() as cur:
    cur.execute('select version()')
    print(cur.fetchone())