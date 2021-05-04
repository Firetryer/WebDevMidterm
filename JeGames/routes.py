import datetime
from flask import render_template, url_for, flash, redirect, request, session
from flask_login import login_user, logout_user, current_user, login_required
from JeGames.forms import RegisterForm, LoginForm
from JeGames.models import AppUser
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
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if form.validate_on_submit():
        user = AppUser.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            if next_page == "logout":
                next_page = "index"
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash("You have entered an invalid username or password", "flash_error")

    return render_template("signin.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login_page'))


@app.route("/create_account", methods=["POST", "GET"])
def create_account_page():
    form = RegisterForm(request.form)
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        register_date = datetime.datetime.now()
        hashed = bcrypt.generate_password_hash(form.password.data)

        new_user = AppUser(
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

@app.route("/admin_page")
@login_required
def admin_page():
    if current_user.admin == False:
        return redirect(url_for("index"))
    else:
        return render_template("admin_page.html")