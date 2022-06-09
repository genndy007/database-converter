import peewee as pw
from playhouse.mysql_ext import MySQLConnectorDatabase
from app.db import CACHE_DIR
from app.db.orm import (
    POSTGRES_CONNECTION_DATA,
    MYSQL_CONNECTION_DATA,
    DB_NAME,
    SQLITE_DB_FILE_NAME
)

database_proxy = pw.DatabaseProxy()

db1 = pw.SqliteDatabase(f'{CACHE_DIR}/{SQLITE_DB_FILE_NAME}')
db2 = pw.PostgresqlDatabase(DB_NAME, **POSTGRES_CONNECTION_DATA)
db3 = MySQLConnectorDatabase(DB_NAME, **MYSQL_CONNECTION_DATA)


class BaseModel(pw.Model):
    class Meta:
        database = database_proxy


class Customer(BaseModel):
    full_name = pw.CharField()
    address = pw.CharField()
    email = pw.CharField()


class Supplier(BaseModel):
    company_name = pw.CharField()
    phone_number = pw.CharField()


class Hardware(BaseModel):
    supplier = pw.ForeignKeyField(Supplier)
    item_name = pw.CharField()
    price = pw.FloatField()
    amount = pw.IntegerField()


class Purchase(BaseModel):
    customer = pw.ForeignKeyField(Customer)
    hardware = pw.ForeignKeyField(Hardware)
    amount = pw.IntegerField()
    total_price = pw.FloatField()


models_list = [Customer, Supplier, Hardware, Purchase]


def init_hw_db_orm():
    database_proxy.initialize(db1)
    db1.connect()
    db1.create_tables(models_list)

    for letter in 'abcde':
        Customer.create(full_name=f'{letter * 3}',
                        address=f'country {letter}',
                        email=f'{letter}@{letter}.com')

    for num in range(5):
        Supplier.create(company_name=f'company {num}', phone_number=f'+{str(num) * 9}')

    for customer, supplier in zip(Customer.select(), Supplier.select()):
        hardware = Hardware.create(supplier=supplier,
                                   item_name=customer.full_name,
                                   price=100,
                                   amount=200)
        Purchase.create(customer=customer,
                        hardware=hardware,
                        amount=2,
                        total_price=hardware.price * 2)


def get_all_customers_dicts(db: pw.SqliteDatabase | pw.PostgresqlDatabase | MySQLConnectorDatabase = db1):
    database_proxy.initialize(db)
    db.connect(reuse_if_open=True)

    return [row for row in Customer.select().dicts()]







