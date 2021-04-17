# from flask import Flask
# from flask_restful import Resource, Api

# app = Flask(__name__)
# api = Api(app)

# class Main(Resource):
#     def get(self):
#         return {'message': 'success'}, 200

# api.add_resource(Main, '/')

# if __name__ == '__main__':
#     app.run(debug=True)

import json
import time
import threading
from datetime import datetime
from websocket import create_connection

class CandleSticker(threading.Thread):

    def __init__(self, minutes, **kwargs):
        super(CandleSticker, self).__init__(**kwargs)
        self.minutes = minutes

    def run(self):
        while True:
            prices = self.listen_forever()
            converted_criptos = [float(i) for i in prices]

            open_value = converted_criptos[0]
            close_value = converted_criptos[-1]
            max_value = max(converted_criptos)
            min_value = min(converted_criptos)
            date_hour = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

            print(f'{self.minutes} minuto(s) - abertura: {open_value}, fechamento: {close_value}, maxima: {max_value}, minimo: {min_value}, data-hora: {date_hour}')

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

try:
    CandleSticker(1).start()
    CandleSticker(5).start()
    CandleSticker(10).start()
except Exception as e:
    print(f'Exception occured: {e}')
