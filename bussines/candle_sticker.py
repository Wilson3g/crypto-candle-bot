from models.candle_sticker import CandleStickerModel
from schema.candle_sticker import CandleStickerSchema
from flask_restful import Resource
from websocket import create_connection
from datetime import datetime
import threading
import time
import json


candle_schema = CandleStickerSchema()


class CandleStickerBussines(threading.Thread, Resource):
    def __init__(self, minutes=None, **kwargs):
        super(CandleStickerBussines, self).__init__(**kwargs)
        self.minutes = minutes
        self._running = True

    def run(self):
        while self._running:
            prices = self.listen_forever()
            converted_criptos = [float(i) for i in prices]
        
            candle = {
                'open_value': converted_criptos[0],
                'close_value': converted_criptos[-1],
                'max_value': max(converted_criptos),
                'min_value': min(converted_criptos),
                'periodicity': self.minutes,
                'date_time': datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            }
            CandleStickerModel.insert_candle_sticker(candle)
            print(f'Captura de {self.minutes} minuto(s) realizada')

            if self._running == False:
                return

    def stop(self):
        self._running = False

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

    def post(self):
        self.__class__(1).start()
        self.__class__(5).start()
        self.__class__(10).start()
        return {'message': 'Iniciando criação de candlestickers'}, 200

    def get(self):
        result = CandleStickerModel.query.order_by(CandleStickerModel.id.desc()).all()
        return candle_schema.dump(result, many=True), 200
