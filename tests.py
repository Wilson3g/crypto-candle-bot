import unittest
import time
import json
from datetime import datetime
from app import create_app
from bussines.candle_sticker import CandleStickerBussines


class CandleStickerTest(unittest.TestCase):

    def setUp(self):
        app = create_app().test_client()
        proc = CandleStickerBussines(0.1)
        self.proc = proc
        self.app = app

    def test_get_candle(self):
        app = self.app
        self.proc
        time.sleep(5)
        response = app.post('/candle-sticke')
        candle = json.loads(response.data)
        self.assertEqual(200, response.status_code)
        self.assertEqual(list, type(candle))
        self.assertEqual('1', candle[0].get('periodicity'))
        self.assertEqual(1, candle[0].get('id'))

if __name__ == '__main__':
    unittest.main()
