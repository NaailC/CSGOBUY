from flask import url_for 
from unittest.mock import patch
from flask_testing import TestCase

from application import app
from application.routes import Buy

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///")
        return app

class TestResponse(TestBase):
    def test_get_buy(self):
        with patch('random.choice') as random:
            random.return_value = 'AK'
            response = self.client.get(url_for('get_buy'))
            self.assertEquals(b'AK', response.data)