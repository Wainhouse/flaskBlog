from flask import Blueprint, render_template


views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html" )

@views.route("/logout")
def home():
    return render_template("logout.html")


@views.route("/login")
def home():
    return render_template("login.html")


@views.route("/sign-up")
def home():
    return render_template("sign-up.html")        