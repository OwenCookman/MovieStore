import requests
import os
from flask import Flask, render_template, request

app = Flask(__name__)


def search_result(search_text):
    resp = requests.get(url="http://openlibrary.org/search.json?q=" +
                        search_text + "&mode=ebooks&has_fulltext=true")
    json = resp.json()
    xx = json['docs']
    for item in xx:
        if 'author_name' in item:
            print(item['title'], item['author_name'])


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/results", methods=["POST"])
def results():
    if request.method == "POST":
        search_text = request.form['search']
        search_result(search_text)
        return render_template("results.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1",
            port=5000,
            debug=True)
