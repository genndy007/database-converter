SQLITE_DB_FILE_NAME = 'hw_storage_orm.sqlite3'
DB_NAME = 'hw_storage_orm'

POSTGRES_CONNECTION_DATA = dict(
    host='localhost',
    user='postgres',
    password='postgres',
    port='5432',
)

MYSQL_CONNECTION_DATA = dict(
    host='localhost',
    user='mysqluser',
    password='mysqlpassword',
)

MYSQL_TABLE_FIELDS = {
    'customers': ('customer_id', 'full_name', 'address'),
    'suppliers': ('supplier_id', 'company_name', 'phone_number'),
    'hardwares': ('hardware_id', 'supplier_id', 'item_name'),
    'purchases': ('purchase_id', 'customer_id', 'hardware_id'),
}
