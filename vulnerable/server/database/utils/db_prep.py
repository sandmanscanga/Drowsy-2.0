"""Module to ensure the database is ready when the flask app starts"""
# pylint: disable=import-error,protected-access

import time

import MySQLdb

from server.database.utils.db_creds import ROOT_CREDS, USER_CREDS
from server.database.utils.db_data import load_users


def wait_for_service(max_wait_time: int = 20) -> None:
    """
    Waits for the MySQL service to accept transactions

    There is a slight timing issue when the docker container for the MySQL
    service, this function will wait for a specified number of seconds
    so the service has enough time to come online.

    Args:
        max_wait_time (:obj:`int`, optional): the number of seconds to wait
                                              before throwing an exception for
                                              lack of an accepted database
                                              connection

    Raises:
        MySQLdb._exceptions.OperationalError: if database connection fails

    """
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


def reinit_db() -> None:
    """
    Drops and recreates the database and table schema from scratch

    Drops the vuln_db database if it exists, selects all MySQL users from the
    mysql.user table in search of vuln_user, drops the vuln_user if the user
    exists, creates the database, creates the user, and grants the user
    privileges.

    Raises:
        MySQLdb._exceptions.OperationalError: if database connection fails

    """

    try:
        db_obj = MySQLdb.connect(**ROOT_CREDS)
        cur = db_obj.cursor()

        cur.execute("DROP DATABASE IF EXISTS vuln_db;")
        cur.execute("CREATE DATABASE vuln_db;")

        cur.execute("SELECT User FROM mysql.user WHERE User='vuln_user';")
        if len(cur.fetchall()) > 0:
            cur.execute("DROP USER 'vuln_user'@'%%';")

        cur.execute("CREATE USER 'vuln_user'@'%%' IDENTIFIED BY 'insecure';")
        cur.execute("GRANT ALL PRIVILEGES ON vuln_db.* TO 'vuln_user'@'%%';")

        cur.execute("FLUSH PRIVILEGES;")
        db_obj.close()
    except MySQLdb._exceptions.OperationalError as err:
        raise err


def populate_db(db_size: int) -> None:
    """
    Populates the database with a variable amount of users

    Given a specified number of total users, the function will load
    all the users into a list of tuples, iterate through that list, and
    inserting them as values into the users table.

    Args:
        db_size (int): the number of users to populate the database with

    Raises:
        MySQLdb._exceptions.OperationalError: if database connection fails

    """

    try:
        db_obj = MySQLdb.connect(**USER_CREDS)
        cur = db_obj.cursor()

        cur.execute("DROP TABLE IF EXISTS users;")
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

        db_obj.commit()
        db_obj.close()
    except MySQLdb._exceptions.OperationalError as err:
        raise err


def db_prep(db_size: int) -> None:
    """
    Wraps the needed functions in a single master routine

    This is the main backbone of the server, it will wait for the MySQL
    service to come online, it will reinitialize the remote database, and
    it will populate the database.

    Args:
        db_size (int): the number of users to populate into the database with

    """

    wait_for_service()
    reinit_db()
    populate_db(db_size)
