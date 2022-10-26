from pytz import timezone
from . import db
from flask_login import UserMixin 
from sqlalchemy.sql import func



class User(db.Model, UserMixin):
    id = db.column(db.Integer, primary_key = True)
    email = db.column(db.String(150), unique=True)
    username = db.column(db.String(150), unique=True)
    password = db.column(db.String(150))
    date_created = db.colum(db.date(timezone=True), default=func.now)