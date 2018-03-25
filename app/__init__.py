#!/var/www/flask-buzz-web/venv/bin/python
# coding=utf-8

import os

from config import config
from flask_jsglue import JSGlue
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate(render_as_batch=True)
lm = LoginManager()
jsglue = JSGlue()
csrf = CSRFProtect()


def create_app(config_name=None):
    """
    Creates a factory application with all the settings.(Allowing there to be multiple instances.) Also disable csrf for testing.
    Then register blueprints and views.
    :param config_name: The configuration name like Production, development, or testing.
    :param db_ref: Used to celery to run database transactions.
    :return: the factory app.
    """
    if config_name is None:
        config_name = os.environ.get('FLASK_CONFIG', 'development')

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    lm.init_app(app)
    jsglue.init_app(app)
    if config_name != 'testing':
        csrf.init_app(app)

    app.static_folder = 'static'
    app.debug = True

    from app.main import main
    app.register_blueprint(main)

    return app
