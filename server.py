#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, session, redirect, request
from flask_socketio import SocketIO, emit

app = Flask(__name__, static_url_path = "/static")
app.config['SECRET_KEY'] = 'AngusYoung'
socketio = SocketIO(app)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if 'username' in session:
        print "username already in session, redirecting to chat"
        return redirect(url_for("chat"))

    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        print "username insert into session"
        return redirect(url_for("chat"))
    return render_template("login.html")

@app.route("/")
def chat():
    if 'username' not in session:
        print "username not in session, redirecting to login"
        return redirect(url_for("login"))
    print "username in session, rendering to chat"
    return render_template("home.html", user = session['username'])

@socketio.on('mymessage')
def message(msg):
    print msg["author"] + ": " + msg["msg"]
    emit('brmsg', {'text': msg['msg'], 'author': msg['author']}, broadcast = True)

@socketio.on('connection')
def connection(data):
    print data["data"]



if __name__ == "__main__":
    socketio.run(app, host = '0.0.0.0', port=8080)
