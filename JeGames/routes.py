from flask import render_template, url_for, flash, redirect, request, send_from_directory
from flask_login import login_user, logout_user, current_user, login_required
from JeGames import app, db, bcrypt 


@app.route("/")
def index():
    return render_template("index.html")