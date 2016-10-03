#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for

app = Flask(__name__, static_url_path = "/static")
app.debug = True

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/chat/<user>")
def chat(user):
    return render_template("chat.html", user = user)

if __name__ == "__main__":
    app.run(port=8080)
