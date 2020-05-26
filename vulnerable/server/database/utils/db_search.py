"""Module for executing search queries against the database"""
# pylint: disable=import-error,protected-access
import json
import MySQLdb
from server.logger.main import LOGGER
from server.database.utils.db_creds import USER_CREDS

logger = LOGGER.get_logger(alias="db_search")


def db_search(query, by_name=True):
    """Executes a SQL query against the database"""
    try:
        db_obj = MySQLdb.connect(**USER_CREDS)
        cur = db_obj.cursor()
        if by_name:
            sql = "SELECT first_name, last_name FROM users WHERE last_name LIKE '%s%%';" % query
        else:
            sql = "SELECT first_name, last_name FROM users WHERE id=%s AND id IS NOT NULL;" % query
        logger.debug(json.dumps({"raw": query, "sql": sql}, indent=2))
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
    except MySQLdb._exceptions.OperationalError as err:
        logger.error(str(err))
        raise err
