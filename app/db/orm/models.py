import peewee as pw

from app.db import CACHE_DIR

DB_FILE_NAME = 'hw_storage_orm.sqlite3'

db1 = pw.SqliteDatabase(f'{CACHE_DIR}/{DB_FILE_NAME}')


class Customer(pw.Model):
    full_name = pw.CharField()
    address = pw.CharField()
    email = pw.CharField()

    class Meta:
        database = db1
        table_name = 'customers'


class Supplier(pw.Model):
    company_name = pw.CharField()
    phone_number = pw.CharField()

    class Meta:
        database = db1
        table_name = 'suppliers'


class Hardware(pw.Model):
    supplier = pw.ForeignKeyField(Supplier)
    item_name = pw.CharField()
    price = pw.FloatField()
    amount = pw.IntegerField()

    class Meta:
        database = db1
        table_name = 'hardwares'


class Purchase(pw.Model):
    customer = pw.ForeignKeyField(Customer)
    hardware = pw.ForeignKeyField(Hardware)
    amount = pw.IntegerField()
    total_price = pw.FloatField()

    class Meta:
        database = db1
        table_name = 'purchases'


def init_hw_db_orm():
    db1.connect()
    db1.create_tables([Customer, Supplier, Hardware, Purchase])

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