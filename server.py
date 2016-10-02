#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(port=8080)
