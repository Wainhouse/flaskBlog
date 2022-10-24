from flask import Blueprint


views = Blueprint("views", __name__)

@views.route("/login")
def login():
    return "Login"

@views.route("/sign-up")
def sign_up():
    return "Sign Up"

@views.route("/logout")
def logout():
    return "Logout"