"""Module for executing search queries against the database"""
# pylint: disable=import-error,protected-access
import json
import MySQLdb
from server.logger.main import LOGGER
from server.database.utils.db_creds import USER_CREDS

logger = LOGGER.get_logger(alias="db_search")


def db_search(query, by_name=True):
    """Executes a SQL query against the database

    The main driver for searching the database full of users.  Every
    query that is executed on the database is logged to a rotating
    file handler.  Search can be executed both by id and by last name.

    Args:
        query (str): a string containing the user query
        by_name (:obj:`bool`, optional): search setting to execute the
            query using the id or using the last name, by default the
            search is executed by last name

    Returns:
        tuple: returns a matrix containing a tuple of tuples

    Raises:
        MySQLdb._exceptions.OperationalError: if database connection fails

    """
    try:
        db_obj = MySQLdb.connect(**USER_CREDS)
        cur = db_obj.cursor()
        if by_name:
            fs_sql = "SELECT first_name, last_name FROM users"\
                " WHERE last_name LIKE '%s%%';"
        else:
            fs_sql = "SELECT first_name, last_name FROM users"\
                " WHERE id=%s AND id IS NOT NULL;"
        sql = fs_sql % query
        logger.debug(json.dumps({"raw": query, "sql": sql}, indent=2))
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
    except MySQLdb._exceptions.OperationalError as err:
        logger.error(str(err))
        raise err
