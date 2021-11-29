#!/usr/bin/env python3

from flask import Flask, session, redirect, url_for, escape, request, render_template
import werkzeug.exceptions
import crypt
import secrets

app = Flask(__name__)
app.secret_key = "secrets.token_bytes(50)"

FLAG = open("/flag.txt").read()

@app.route("/")
def index():
    if "username" not in session:
        return redirect("/login?msg=Login+required")

    if session["username"] == "root":
        return "Hello, %s!<br/>\nHave a nice flag: %s" % (session["username"], FLAG)
    else:
        return "Hello, %s!<br/>\nNo flags available for you."

@app.route("/robots.txt")
def robotstxt():
    return open("robots.txt").read()

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.tpl", msg=request.args.get("msg", ""))

    username = request.form["username"]
    password = request.form["password"]

    # use system logins during beta phase, needs to be moved to database for production use!
    users = dict(x.split(":")[:2] for x in open("/etc/shadow").readlines() if x.split(":")[1][0] != "!")
    if username not in users:
        return redirect("/login?msg=Invalid+credentials")
    if crypt.crypt(password, users[username]) != users[username]:
        return redirect("/login?msg=Invalid+credentials")

    session["username"] = username
    return redirect("/")

@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return "/app/app.py:app raised an exception:<br/>" + str(e), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
