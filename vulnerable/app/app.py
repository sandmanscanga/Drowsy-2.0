from flask import Flask, render_template, request
from database.db_prep import db_prep
from database.db_search import db_search

db_prep(250)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/search-post", methods=["GET", "POST"])
def search_post():
    if request.method == "POST":
        query = request.form.get("id")
        if query:
            result = db_search(query, by_name=False)
            return render_template("search_post.html", result=result)
    return render_template("search_post.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")