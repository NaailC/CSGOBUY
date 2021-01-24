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
            random.return_value = 'AK'
            response = self.client.get(url_for('get_buy'))
            self.assertEquals(b'AK', response.data)
    
    def test_get_buy2(self):
        with patch('random.choice') as random:
            random.return_value = 'p90'
            response = self.client.get(url_for('get_buy'))
            self.assertEquals(b'p90', response.data)

    def test_get_buy3(self):
        with patch('random.choice') as random:
            random.return_value = 'SG'
            response = self.client.get(url_for('get_buy'))
            self.assertEquals(b'SG', response.data)
