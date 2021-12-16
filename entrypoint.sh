#!/bin/sh

echo "Waiting for app to scrap..."

python app.py

echo "Scrapping started"

FILE=/usr/bin/app/amazon.search.db

if [ -f "$FILE" ]; then
    echo "$FILE exists."
else 
    echo "$FILE does not exist."
fi

echo "sqlite3"

sqlite3

exec "$@"
