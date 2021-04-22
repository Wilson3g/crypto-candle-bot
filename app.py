from flask import Flask
from flask_script import Manager, Server

from extensions import marshmallow
from bussines import routes as config_bus
from extensions.sql_alchemy import db, init_app

def create_app(config_file='settings.py'):
    my_app = Flask(__name__)
    my_app.config.from_pyfile(config_file)

    init_app(my_app)
    marshmallow.ini_app(my_app)
    config_bus.init_app(my_app)

    db.app = my_app
    db.create_all()
    return my_app
