from app.db.sqlite import init_hw_sqlite_db
from app.db.postgres import init_hw_pg_db
from app.db.migrate import migrate_sqlite_to_pg, migrate_pg_to_mysql
from app.db.mysql import recreate_mysql_db, init_hw_mysql_db


recreate_mysql_db()
init_hw_mysql_db()
migrate_pg_to_mysql()





