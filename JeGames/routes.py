from flask import render_template, url_for, flash, redirect, request
from JeGames.forms import RegisterForm
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

@app.route("/create_account", methods=["POST", "GET"])
def create_account_page():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = form.username.data
        hashed = bcrypt.generate_password_hash(form.password.data)
        #new_user = AppUser(username = user, password = hashed)
        #db.session.add(new_user)
        #db.session.commit()
        print("WORKS!")
        flash('Account created succesfully! Login now!', 'flash_success')
        return redirect(url_for('login_page'))
    return render_template("signup.html", form=form)

@app.route("/support")
def support_page():
    return render_template("support.html")

@app.route("/game_page")
def game_page():
    return render_template("game_page.html")