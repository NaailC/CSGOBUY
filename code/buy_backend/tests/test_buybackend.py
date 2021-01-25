from flask_testing import TestCase
from unittest.mock import patch
from flask import url_for
from random import choice
from app import app


class TestBase(TestCase):
    def create_app(self):
        return app
    

class TestResponse(TestBase):
    def test_get_buy(self):
        with patch('random.choice') as random:
            random.return_value = '57'
            response = self.client.get(url_for('get_buy'))
            response2 = self.client.post(url_for('get_buystrength'))
            self.assertIn(b'57', response.data)
    
    def test_get_buy2(self):
        with patch('random.choice') as random:
            random.return_value = 'Scout'
            response = self.client.get(url_for('get_buy'))
            response2 = self.client.post(url_for('get_buystrength'))
            self.assertEquals(b'p90', response.data)

    def test_get_buy3(self):
        with patch('random.choice') as random:
            random.return_value = 'p250'
            response = self.client.get(url_for('get_buy'))
            response2 = self.client.post(url_for('get_buystrength'))
            self.assertEquals(b'p250', response.data)