#!/bin/bash
# Script to debug database issues in CI

echo "=== Checking MySQL Database ==="
mysql -h 127.0.0.1 -P 3306 -u root -proot -e "SHOW DATABASES;"

echo "=== Checking test_db Tables ==="
mysql -h 127.0.0.1 -P 3306 -u root -proot -e "USE test_db; SHOW TABLES;"

echo "=== Checking test_test_db Tables ==="
mysql -h 127.0.0.1 -P 3306 -u root -proot -e "CREATE DATABASE IF NOT EXISTS test_test_db; USE test_test_db; SHOW TABLES;"

echo "=== Django Migrations ==="
cd ISTP_website
python manage.py showmigrations webapp

echo "=== Applying migrations directly to test database ==="
python manage.py migrate --database=default --noinput
mysql -h 127.0.0.1 -P 3306 -u root -proot -e "USE test_test_db; SHOW TABLES;"

echo "=== Test database debug complete ===" 