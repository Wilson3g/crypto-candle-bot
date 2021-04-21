from flask_marshmallow import Marshmallow
from app.models.candle_sticker import CandleStickerModel
from app.extensions.marshmallow import marshmallow as ma



class CandleStickerSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model=CandleStickerModel
        fields=('id', 'open_value', 'close', 'max_value', 
                  'min_value', 'periodicity', 'date_time')
        ordered=True
        load_instance=True
