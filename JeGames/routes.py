from flask import render_template, url_for, flash, redirect, request
from JeGames import app, db, bcrypt 


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/browse_games")
def browse_page():
    return render_template("game_browse.html")

@app.route("/login")
def login_page():
    return render_template("signin.html")

@app.route("/create_account")
def create_account_page():
    return render_template("signup.html")

@app.route("/support")
def support_page():
    return render_template("support.html")

@app.route("/game_page")
def game_page():
    return render_template("game_page.html")