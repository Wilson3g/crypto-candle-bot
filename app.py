from flask import Flask, jsonify
from flask_restful import Resource, Api
from datetime import datetime
from websocket import create_connection
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_marshmallow import Marshmallow
import json
import time
import threading

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

ma = Marshmallow(app)
api = Api(app)


class CandleStickerModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    open_value = db.Column(db.String, nullable=False)
    close_value = db.Column(db.String, nullable=False)
    max_value = db.Column(db.String, nullable=False)
    min_value = db.Column(db.String, nullable=False)
    periodicity = db.Column(db.String, nullable=False)
    date_time = db.Column(db.String, nullable=False)


class CandleStickerSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = CandleStickerModel
        fields = ('id', 'open_value', 'close', 'max_value', 
                  'min_value', 'periodicity', 'date_time')
        ordered = True

candle_schema = CandleStickerSchema()

class CandleSticker(threading.Thread, Resource):
    def __init__(self, minutes=None, **kwargs):
        super(CandleSticker, self).__init__(**kwargs)
        self.minutes = minutes

    def run(self):
        while True:
            prices = self.listen_forever()
            converted_criptos = [float(i) for i in prices]

            candle = CandleStickerModel(
                open_value=converted_criptos[0],
                close_value=converted_criptos[-1],
                max_value=max(converted_criptos),
                min_value=min(converted_criptos),
                periodicity=self.minutes,
                date_time=datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            )

            db.session.add(candle)
            db.session.commit()

            print(f'Captura de {self.minutes} minuto(s) realizada')

    def listen_forever(self):
        try:
            ws = create_connection('wss://api2.poloniex.com')
            ws.send('{"command": "subscribe", "channel": "USDT_BTC"}')
            
            price = []
            t_end = time.time() + 60 * self.minutes
            while time.time() < t_end:
                result = ws.recv()
                result = json.loads(result)

                if len(result) > 1:
                    result = result[2][0]
                    if len(result) != 2:
                        price.append(result[2])

            ws.close()
            return price
        except Exception as ex:
            print(f'exception: {ex}')

    def get(self):
        self.__class__(1).start()
        self.__class__(5).start()
        self.__class__(10).start()
        return {'message': 'Iniciando criação de candlestickers'}, 200

    def post(self):
        result = CandleStickerModel.query.filter_by(periodicity=1).all()
        return candle_schema.dump(result, many=True), 200


api.add_resource(CandleSticker, '/candle-sticke')

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
