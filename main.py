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
from websocket import create_connection

class CandleSticker:
    def create_clandle_stick(self, minutes):
        prices = self.listen_forever(minutes=minutes)
        converted_criptos = [float(i) for i in prices]

        open_value = converted_criptos[0]
        close_value = converted_criptos[-1]
        max_value = max(converted_criptos)
        min_value = min(converted_criptos)

        print(f'{minutes} minuto(s) - abertura: {open_value}, fechamento: {close_value}, maxima: {max_value}, minimo: {min_value}')


    def listen_forever(self, minutes):
        try:
            ws = create_connection('wss://api2.poloniex.com')
            ws.send('{"command": "subscribe", "channel": "USDT_BTC"}')
            
            price = []
            t_end = time.time() + 60 * minutes
            while time.time() < t_end:
                result = ws.recv()
                result = json.loads(result)

                result = result[2][0]
                if len(result) != 2:
                    price.append(result[2])

            ws.close()
            return price
        except Exception as ex:
            print(f'exception: {ex}')


try:
    cancle_sticker = CandleSticker()
    while True:
        cancle_sticker.create_clandle_stick(1)
        cancle_sticker.create_clandle_stick(2)
        cancle_sticker.create_clandle_stick(3)
except Exception as e:
    print(f'Exception occured: {e}')
