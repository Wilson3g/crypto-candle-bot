from flask_marshmallow import Marshmallow

marshmallow = Marshmallow()

def ini_app(app):
    marshmallow.init_app(app)
