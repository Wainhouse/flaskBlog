from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'lwKhartoum!21'
    app.config['SQL_ALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    @app.route("/")
    def home():
        return "<h1>Hello</h1>"
    
    from .views import views
    from .auth import auth


    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Note
    from . import models

    create_database(app)

    return app

def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)    
        print("Created Database!")