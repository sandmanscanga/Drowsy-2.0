from flask import Flask, render_template
import MySQLdb
import os
from database.db_prep import db_prep
from database.db_creds import USER_CREDS

db_prep()


def get_results():
    try:
        db = MySQLdb.connect(**USER_CREDS)
        c = db.cursor()
        c.execute("select first_name, last_name from users;")
        results = [f"{row[0]} {row[1]}" for row in c.fetchall()]
        db.close()
    except MySQLdb._exceptions.OperationalError as e:
        raise e
    else:
        return results


app = Flask(__name__)


@app.route("/")
def index():
    results = get_results()
    return render_template("index.html", results=results)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
