if ! command -v poetry &> /dev/null
then
    echo "poetry could not be found, install via pip or package manager"
    exit
fi

poetry install  # install python deps
./scripts/postgres_recreate.sh    # create postgres db once again
poetry run python ./app/db/postgres.py   # init db