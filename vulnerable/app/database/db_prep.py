import MySQLdb
import time
from database.db_creds import ROOT_CREDS, USER_CREDS


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


def populate_db(users):
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
        for user in users:
            c.execute("INSERT INTO users VALUES %s;" % user)
        db.close()
    except MySQLdb._exceptions.OperationalError as e:
        raise e


def db_prep():
    wait_for_service()
    reinit_db()
    raw_users = (
        ("John", "Doe", "password123"),
        ("Jane", "Smith", "letmein"),
        ("Peter", "Pan", "secret")
    )
    users = []
    for i, u in enumerate(raw_users):
        row = (i+1, repr(u[0]), repr(u[1]), repr(u[2]))
        users.append("(%d, %s, %s, %s)" % row)
    populate_db(users)


if __name__ == "__main__":
    db_prep()
