"""Module to ensure the database is ready when the flask app starts"""
# pylint: disable=import-error,protected-access
import time
import MySQLdb
from server.database.utils.db_creds import ROOT_CREDS, USER_CREDS
from server.database.utils.db_data import load_users


def wait_for_service(max_wait_time=20):
    """Waits for the MySQL service to accept transactions"""
    elapsed_time = 0
    while True:
        elapsed_time += 1
        if elapsed_time >= max_wait_time:
            raise Exception("Max wait time reached waiting for service")
        try:
            db_obj = MySQLdb.connect(**ROOT_CREDS)
        except MySQLdb._exceptions.OperationalError:
            time.sleep(1)
        else:
            db_obj.close()
            break


def reinit_db():
    """Drops and recreates the database and table schema from scratch"""
    try:
        db_obj = MySQLdb.connect(**ROOT_CREDS)
        cur = db_obj.cursor()
        cur.execute("DROP DATABASE IF EXISTS vuln_db;")
        cur.execute("SELECT User FROM mysql.user WHERE User='vuln_user';")
        if len(cur.fetchall()) > 0:
            cur.execute("DROP USER 'vuln_user'@'%%';")
        cur.execute("CREATE DATABASE vuln_db;")
        cur.execute("CREATE USER 'vuln_user'@'%%' IDENTIFIED BY 'insecure';")
        cur.execute("GRANT ALL PRIVILEGES ON vuln_db.* TO 'vuln_user'@'%%';")
        cur.execute("FLUSH PRIVILEGES;")
        db_obj.close()
    except MySQLdb._exceptions.OperationalError as err:
        raise err


def populate_db(db_size):
    """Populates the database with a variable amount of users"""
    try:
        db_obj = MySQLdb.connect(**USER_CREDS)
        cur = db_obj.cursor()
        cur.execute("""
CREATE TABLE users(
    id INTEGER NOT NULL PRIMARY KEY,
    first_name VARCHAR(1000) NOT NULL,
    last_name VARCHAR(1000) NOT NULL,
    password VARCHAR(1000) NOT NULL
);
        """)
        users = load_users(db_size)
        for user in users:
            cur.execute("INSERT INTO users VALUES %s;" % user)
        db_obj.close()
    except MySQLdb._exceptions.OperationalError as err:
        raise err


def db_prep(db_size):
    """Wraps the needed functions in a single master routine"""
    wait_for_service()
    reinit_db()
    populate_db(db_size)
