#### Steps
- Pull the code
- python3 -m venv venv
- source venv/bin/activate
- pip3 install mysql-connector-python
- docker-compose up -d
    - If there is an issue Docker-compose : mysqld: Can't create/write to file '/var/lib/mysql/is_writable' (Errcode: 13 - Permission denied)
    - RUN :- chown 999:999 mysql_data_container
- python test_update.py
