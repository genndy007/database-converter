from app.db.sqlite import SQLite

with SQLite() as cur:
    for row in cur.execute('select sqlite_version();'):
        print(row)