import MySQLdb
import time
from server.database.utils.db_creds import ROOT_CREDS, USER_CREDS
from server.database.utils.db_data import load_users


def wait_for_service(max_wait_time=20):
    elapsed_time = 0
    while True:
        elapsed_time += 1
        if elapsed_time >= max_wait_time:
            raise Exception("Max wait time reached waiting for service")
        try:
            db = MySQLdb.connect(**ROOT_CREDS)
        except MySQLdb._exceptions.OperationalError:
            time.sleep(1)
        else:
            db.close()
            break


def reinit_db():
    try:
        db = MySQLdb.connect(**ROOT_CREDS)
        c = db.cursor()
        c.execute("DROP DATABASE IF EXISTS vuln_db;")
        c.execute("SELECT User FROM mysql.user WHERE User='vuln_user';")
        if len(c.fetchall()):
            c.execute("DROP USER 'vuln_user'@'%%';")
        c.execute("CREATE DATABASE vuln_db;")
        c.execute("CREATE USER 'vuln_user'@'%%' IDENTIFIED BY 'insecure';")
        c.execute("GRANT ALL PRIVILEGES ON vuln_db.* TO 'vuln_user'@'%%';")
        c.execute("FLUSH PRIVILEGES;")
        db.close()
    except MySQLdb._exceptions.OperationalError as e:
        raise e


def populate_db(db_size):
    try:
        db = MySQLdb.connect(**USER_CREDS)
        c = db.cursor()
        c.execute("""
CREATE TABLE users(
    id INTEGER NOT NULL PRIMARY KEY,
    first_name VARCHAR(1000) NOT NULL,
    last_name VARCHAR(1000) NOT NULL,
    password VARCHAR(1000) NOT NULL
);
        """)
        users = load_users(db_size)
        for user in users:
            c.execute("INSERT INTO users VALUES %s;" % user)
        db.close()
    except MySQLdb._exceptions.OperationalError as e:
        raise e


def db_prep(db_size):
    wait_for_service()
    reinit_db()
    populate_db(db_size)
