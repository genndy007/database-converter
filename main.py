from app.db.admin import Admin



admin = Admin()
# new_id = admin.customers.delete(8)
# print(new_id)

new_id = admin.suppliers.create('alsasd', 'lol')
lst = admin.suppliers.get_all()
print(lst)




