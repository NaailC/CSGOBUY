from flask import url_for 
from unittest.mock import patch
from flask_testing import TestCase
import requests_mock

from application import app, db
from application.routes import Buy

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///")
        return app
    
    def setUp(self):
        db.create_all()
        db.session.add(Buy(weapon='testweapon', strat='teststrat', power='testp'))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestResponse(TestBase):

    def test_AK(self):
        with requests_mock.mock() as m:
            m.get('http://CSGOBUY-buy_backend:5001/get/buy', text='AK')
            m.post('http://CSGOBUY-buy_backend:5001/post/buystrength', text='100') 
            m.get('http://CSGOBUY-strat_backend:5002/get/strat', text='Rush A')
            m.post('http://CSGOBUY-strat_backend:5002/post/stratstrength', text='50')
            m.post('http://CSGOBUY-round_strength:5003/post/roundstrength', text='75')
            response = self.client.get(url_for('home'))
            self.assertIn(b'buy AK and Rush A', response.data)
            self.assertIn(b'testweapon and teststrat - power-level testp', response.data)

    def test_P90(self):
        with requests_mock.mock() as m:
            m.get('http://CSGOBUY-buy_backend:5001/get/buy', text='p90')
            m.post('http://CSGOBUY-buy_backend:5001/post/buystrength', text='60') 
            m.get('http://CSGOBUY-strat_backend:5002/get/strat', text='Rush B')
            m.post('http://CSGOBUY-strat_backend:5002/post/stratstrength', text='60')
            m.post('http://CSGOBUY-round_strength:5003/post/roundstrength', text='60')
            response = self.client.get(url_for('home'))
            self.assertIn(b'buy p90 and Rush B', response.data)
            self.assertIn(b'testweapon and teststrat - power-level testp', response.data)
