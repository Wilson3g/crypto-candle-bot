from flask_sqlalchemy import SQLAlchemy
from extensions.sql_alchemy import db


class CandleStickerModel(db.Model):
    __tablename__ = 'candle_sticker'
    id = db.Column(db.Integer, primary_key=True)
    open_value = db.Column(db.String(100), nullable=False)
    close_value = db.Column(db.String(100), nullable=False)
    max_value = db.Column(db.String(100), nullable=False)
    min_value = db.Column(db.String(100), nullable=False)
    periodicity = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.String(100), nullable=False)


    def insert_candle_sticker(candle: dict) -> None:
        candle = CandleStickerModel(**candle)
        db.session.add(candle)
        db.session.commit()
