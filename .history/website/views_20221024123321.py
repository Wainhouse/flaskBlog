from flask import Blueprint, render_template, redirect, url_for


views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html" )

@views.route("/logout")
def logout():
    return redirect(url_for("views.home"))


@views.route("/login")
def login():
    return render_template("login.html")


@views.route("/sign-up")
def signup():
    return render_template("signup.html")        