#!/bin/bash

echo "$MYSQL_DATABASE"

# Путь к CSV-файлу
CSV_FILE="/data.csv"

# Команда для импорта данных в базу данных
mysqlimport --host=db --port=3306 --user="root" --password="$MYSQL_ROOT_PASSWORD" --ignore-lines=1 --fields-terminated-by=',' --lines-terminated-by='\n' $MYSQL_DATABASE $CSV_FILE

tail -f /dev/null