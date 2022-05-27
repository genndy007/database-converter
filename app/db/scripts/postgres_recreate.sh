DB_NAME=hw_storage
DB_USER=postgres

set +e
dropdb $DB_NAME -U $DB_USER || true
createdb $DB_NAME -O $DB_USER -U $DB_USER