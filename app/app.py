from flask import Flask
from flask_script import Manager, Server

from app.extensions import migrate
from app.extensions import marshmallow
from . import bussines as config_bus
from app.extensions.sql_alchemy import db, init_app

def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    init_app(app)
    marshmallow.ini_app(app)
    migrate.init_app(app, db)
    config_bus.init_app(app)

    db.app = app
    db.create_all()
    return app
