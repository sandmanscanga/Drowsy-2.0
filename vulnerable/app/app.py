from flask import Flask, render_template, request
from urllib.parse import unquote_plus
from database.db_prep import db_prep
from database.db_search import db_search

db_prep(250)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/search-get", methods=["GET"])
def search_get():
    if request.method == "GET" and request.query_string:
        raw_query = request.query_string.decode("utf-8")
        query_dict = {}
        for fields in raw_query.split("&"):
            field = fields.split("=")
            query_dict[field[0]] = field[1] if len(field) <= 2 else "=".join(field[1:])
        if "last_name" in query_dict:
            _query = query_dict.get("last_name")
            query = unquote_plus(_query)
            if query:
                result = db_search(query)
                return render_template("search_get.html", result=result)
    return render_template("search_get.html")


@app.route("/search-get-blind", methods=["GET"])
def search_get_blind():
    if request.method == "GET" and request.query_string:
        raw_query = request.query_string.decode("utf-8")
        query_dict = {}
        for fields in raw_query.split("&"):
            field = fields.split("=")
            query_dict[field[0]] = field[1] if len(field) <= 2 else "=".join(field[1:])
        if "id" in query_dict:
            _query = query_dict.get("id")
            query = unquote_plus(_query)
            if query:
                result = db_search(query, by_name=False)
    return render_template("search_get_blind.html")


@app.route("/search-post", methods=["GET", "POST"])
def search_post():
    if request.method == "POST":
        query = request.form.get("id")
        if query:
            result = db_search(query, by_name=False)
            return render_template("search_post.html", result=result)
    return render_template("search_post.html")


@app.route("/search-post-blind", methods=["GET", "POST"])
def search_post_blind():
    if request.method == "POST":
        query = request.form.get("last_name")
        if query:
            result = db_search(query)
    return render_template("search_post_blind.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
