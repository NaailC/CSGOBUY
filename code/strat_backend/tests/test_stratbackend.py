from flask_testing import TestCase
from unittest.mock import patch
from flask import url_for
from random import  choice

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_strat(self):
            with patch("random.choice") as random:
                random.return_value = 'Rush A'
                response = self.client.get(url_for('/get/strat'))
                self.assertIn(b'Rush A', response.data)

    def test_get_strat2(self):
            with patch("random.choice") as random:
                random.return_value = 'Rush B'
                response = self.client.get(url_for('/get/strat'))
                self.assertIn(b'Rush B', response.data)