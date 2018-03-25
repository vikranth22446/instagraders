# coding=utf-8

from flask import render_template, g, request, url_for
from flask_login import login_required, current_user

from app import lm, db
from app.main import main


class User(db.Model):
    __tablename__ = "user"
    username = db.Column(db.String,primary_key=True)
    password = db.Column(db.String)


@main.before_app_request
def before_request():
    """
    Saves the current user globally.
    """
    if current_user.is_authenticated:
        g.user = current_user


@lm.user_loader
def load_user(user_id):
    """
    Tries to Load the User.
    :param user_id:
    :return:
    """
    try:
        return User.query.get(user_id)
    except Exception as e:
        print(e)
        return None


@main.route('/')
def index():
    return render_template('index.html')
