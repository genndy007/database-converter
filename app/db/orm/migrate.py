from playhouse.mysql_ext import MySQLConnectorDatabase
import peewee as pw

from app.db.orm.models import (
    db1, db2, db3, database_proxy,
    Customer, Supplier, Hardware, Purchase, models_list,
    get_all_customers_dicts
)


def migrate_db(db1: pw.SqliteDatabase | pw.PostgresqlDatabase | MySQLConnectorDatabase,
               db2: pw.SqliteDatabase | pw.PostgresqlDatabase | MySQLConnectorDatabase):
    database_proxy.initialize(db1)
    conn_status = db1.connect(reuse_if_open=True)

    table_data = {}
    for model in models_list:
        table_data[model] = [row for row in model.select().dicts()]

    database_proxy.initialize(db2)
    conn_status = db2.connect(reuse_if_open=True)

    db2.drop_tables(models_list)
    db2.create_tables(models_list)
    with db2.atomic():
        for model in models_list:
            model.insert_many(table_data[model]).execute()


def migrate_sqlite_to_postgres_orm():
    migrate_db(db1, db2)


# move only 3 fields, 3 entries to change
def migrate_postgres_to_mysql_orm():
    # 1. move all
    migrate_db(db2, db3)
    database_proxy.initialize(db3)
    db3.connect(reuse_if_open=True)
    # 2. nullify needed
    Customer.update(email=None).execute()
    Hardware.update(price=None, amount=None).execute()
    Purchase.update(amount=None, total_price=None).execute()
    # 3. change 3 fields
    for pk in (1,2,3):
        Customer.update(address=pw.fn.CONCAT('Updated ', Customer.address)).where(Customer.id == pk).execute()
        Supplier.update(company_name=pw.fn.CONCAT('Updated ', Supplier.company_name)).where(Supplier.id == pk).execute()
        Hardware.update(item_name=pw.fn.CONCAT('Updated ', Hardware.item_name)).where(Hardware.id == pk).execute()

