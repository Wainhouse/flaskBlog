from crypt import methods
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user


views = Blueprint("views", __name__)



@views.route("/")
@views.route("/home")
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route("/create-post", methods=['GET', 'POST'])
@login_required
def create_post():
    return render_template('create_posts.html', user=current_user)