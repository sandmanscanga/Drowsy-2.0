import MySQLdb
from database.db_creds import USER_CREDS


def db_search(query, by_name=True):
    try:
        db = MySQLdb.connect(**USER_CREDS)
        c = db.cursor()
        if by_name:
            sql = "SELECT first_name, last_name FROM users WHERE last_name LIKE '%s%%';" % query
        else:
            sql = "SELECT first_name, last_name FROM users WHERE id=%s AND id IS NOT NULL;" % query
        c.execute(sql)
        rows = c.fetchall()
        print("Results:", rows)
        return rows
    except MySQLdb._exceptions.OperationalError as e:
        raise e
