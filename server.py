#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for
from flask_socketio import SocketIO, emit

app = Flask(__name__, static_url_path = "/static")
app.config['SECRET_KEY'] = 'AngusYoung'
socketio = SocketIO(app)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/chat/<user>")
def chat(user):
    return render_template("home.html", user = user)

@socketio.on('mymessage')
def message(msg):
    print msg["author"] + ": " + msg["msg"]
    emit('brmsg', {'text': msg['msg'], 'author': msg['author']}, broadcast = True)

@socketio.on('connection')
def connection(data):
    print data["data"]



if __name__ == "__main__":
    socketio.run(app, host = '0.0.0.0', port=8080)
