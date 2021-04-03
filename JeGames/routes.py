from flask import render_template, url_for, flash, redirect, request
from JeGames import app, db, bcrypt 


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/browse_games")
def browse_page():
    return render_template("game_browse.html")