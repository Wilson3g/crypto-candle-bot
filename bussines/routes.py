from flask_restful import Api
from bussines.candle_sticker import CandleStickerBussines

api = Api()

def init_app(app):
    api.init_app(app)
    app.api=api


api.add_resource(CandleStickerBussines, '/candle-sticke')
