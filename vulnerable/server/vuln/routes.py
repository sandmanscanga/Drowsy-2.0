"""Module containing the routes for the Flask application"""
# pylint: disable=import-error
from urllib.parse import unquote_plus
from flask import render_template, request
from server.vuln.blueprint import vulns
from server.database.utils.db_search import db_search


@vulns.route("/", methods=["GET"])
def index():
    """Renders the homepage

    This is the homepage, it renders a simple welcome message.

    """
    return render_template("index.html")


@vulns.route("/search-get", methods=["GET"])
def search_get():
    """Standard search using GET method by last_name

    This is the standard search using the GET method in the form,
    along with the search parameter which is by last_name.

    """
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


@vulns.route("/search-get-blind", methods=["GET"])
def search_get_blind():
    """Blind search using GET method by id

    This is the blind search using the GET method in the form, along
    with the search parameter which is id.

    """
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
                _ = db_search(query, by_name=False)
    return render_template("search_get_blind.html")


@vulns.route("/search-post", methods=["GET", "POST"])
def search_post():
    """Standard search using POST method by id

    This is the standard search using the POST method in the form, along
    with the search parameter which is id.

    """
    if request.method == "POST":
        query = request.form.get("id")
        if query:
            result = db_search(query, by_name=False)
            return render_template("search_post.html", result=result)
    return render_template("search_post.html")


@vulns.route("/search-post-blind", methods=["GET", "POST"])
def search_post_blind():
    """Blind search using POST method by last_name

    This is the blind search using the POST method in the form, along
    with the search parameter which is last_name.

    """
    if request.method == "POST":
        query = request.form.get("last_name")
        if query:
            _ = db_search(query)
    return render_template("search_post_blind.html")
