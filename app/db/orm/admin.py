from typing import Type

from app.db.orm.models import (
    database_proxy, db1,
    Customer, Supplier, Hardware, Purchase
)

DBModel = Type[Customer] | Type[Supplier] | Type[Hardware] | Type[Purchase]


class Entity:
    def __init__(self, model: DBModel):
        database_proxy.initialize(db1)
        db1.connect(reuse_if_open=True)

        self.model = model

    def create(self, **kwargs):
        self.model.create(**kwargs)

    def delete(self, pk):
        self.model.delete().where(self.model.id == pk).execute()

    def get_all(self):
        return [row for row in self.model.select().dicts()]


class CustomerEntity(Entity):
    def __init__(self):
        super().__init__(Customer)

    def create(self, full_name, address, email):
        super().create(full_name=full_name, address=address, email=email)


class SupplierEntity(Entity):
    def __init__(self):
        super().__init__(Supplier)

    def create(self, company_name, phone_number):
        super().create(company_name=company_name, phone_number=phone_number)


class HardwareEntity(Entity):
    def __init__(self):
        super().__init__(Hardware)

    def create(self, supplier, item_name, price, amount):
        super().create(supplier=supplier, item_name=item_name, price=price, amount=amount)


class PurchaseEntity(Entity):
    def __init__(self):
        super().__init__(Purchase)

    def create(self, customer, hardware, amount, total_price):
        super().create(customer=customer, hardware=hardware, amount=amount, total_price=total_price)


class DBAdmin:
    def __init__(self):
        self.customer = CustomerEntity()
        self.supplier = SupplierEntity()
        self.hardware = HardwareEntity()
        self.purchase = PurchaseEntity()



