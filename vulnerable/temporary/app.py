from flask import Flask, render_template
import MySQLdb


def get_rows():
    creds = {
        "user": "root",
        "passwd": "topsecret",
        "host": "db"
    }
    db = MySQLdb.connect(**creds)
    c = db.cursor()
    c.execute("select concat('It is working!')")
    rows = c.fetchall()
    return rows[0][0]


app = Flask(__name__)


@app.route('/')
def index():
    result = get_rows()
    return render_template('index.html', result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
