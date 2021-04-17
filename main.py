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

class Subscriber:
    def sum_values(self):
        prices = self.listen_forever()
        converted_criptos = [float(i) for i in prices]
        print(converted_criptos)
        open_close = converted_criptos[::len(converted_criptos)-1]
        high_value = max(converted_criptos)
        lower_value = min(converted_criptos)
        print(f'abertura: {converted_criptos} fechamento: {converted_criptos} minimo: {lower_value} maximo: {high_value}')

    def listen_forever(self):
        try:
            ws = create_connection('wss://api2.poloniex.com')
            ws.send('{"command": "subscribe", "channel": "USDT_BTC"}')
            
            price = []
            t_end = time.time() + 10
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
    Subscriber().sum_values()
except Exception as e:
    print(f'Exception occured: {e}')
