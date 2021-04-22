import datetime
from flask import render_template, url_for, flash, redirect, request, session
from JeGames.forms import RegisterForm, LoginForm
from JeGames.models import User
from JeGames import app, db, bcrypt 


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/browse_games")
def browse_page():
    return render_template("game_browse.html")

@app.route("/login", methods=["POST", "GET"])
def login_page():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['username'] = user.username
            return redirect(url_for('index'))
        else:
            flash("You have entered an invalid username or password", "flash_error")
            return redirect(url_for('login_page'))
    return render_template("signin.html", form=form)

@app.route("/create_account", methods=["POST", "GET"])
def create_account_page():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        register_date = datetime.datetime.now()
        hashed = bcrypt.generate_password_hash(form.password.data)

        new_user = User(
            username = username,
            password = hashed,
            email = email,
            register_date = register_date,
            admin = 0
            )

        db.session.add(new_user)
        db.session.commit()
        flash('Account created succesfully! Login now!', 'flash_success')
        return redirect(url_for('login_page'))
    return render_template("signup.html", form=form)

@app.route("/support")
def support_page():
    return render_template("support.html")

@app.route("/game_page")
def game_page():
    return render_template("game_page.html")