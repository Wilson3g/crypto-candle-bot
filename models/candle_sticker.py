from flask_sqlalchemy import SQLAlchemy
from extensions.sql_alchemy import db


class CandleStickerModel(db.Model):
    __tablename__ = 'candle_sticker'
    id = db.Column(db.Integer, primary_key=True)
    open_value = db.Column(db.Float(40), nullable=False)
    close_value = db.Column(db.Float(40), nullable=False)
    max_value = db.Column(db.Float(40), nullable=False)
    min_value = db.Column(db.Float(40), nullable=False)
    periodicity = db.Column(db.Integer, nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)


    def insert_candle_sticker(candle: dict) -> None:
        candle = CandleStickerModel(**candle)
        db.session.add(candle)
        db.session.commit()
