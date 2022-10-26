from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user


views = Blueprint("views", __name__)


@views.route("/")
def home1():
    return render_template("home.html", name=current_user.username )

@views.route("/home")
def home():
    return render_template("home.html", name=current_user.username )

@views.route("/logout")
def logout():
    return redirect(url_for("views.home"))


@views.route("/login")
def login():
    return render_template("login.html")


@views.route("/sign-up")
def signup():
    return render_template("signup.html")        