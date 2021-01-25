from flask_testing import TestCase
from unittest.mock import patch
from flask import url_for
from random import  choice
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_strat(self):
            with patch("random.choice") as random:
                random.return_value = '4 A'
                response = self.client.get(url_for('get_tstrat'))
                response2 = self.client.post(url_for('get_tstratstrength'))
                self.assertIn(b'4 A', response.data)

    def test_get_strat2(self):
            with patch("random.choice") as random:
                random.return_value = 'Hold B'
                response = self.client.get(url_for('get_tstrat'))
                response2 = self.client.post(url_for('get_tstratstrength'))
                self.assertIn(b'Hold B', response.data)