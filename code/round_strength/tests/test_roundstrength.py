from flask_testing import TestCase
from unittest.mock import patch
from flask import url_for
from random import choice

class TestBase(TestCase):
    def create_app(self):
        return app
    
class TestResponse(TestBase):
    
    def test_roundstrength(self):
        response = self.client.post(url_for('/post/roundstrength'), json={"buystrength" : "50", "stratstrength" : '0'})
        print(response)
        self.assertIn(b'Your power-level is 25%', response.data)
    
    def test_roundstrength1(self):
        response = self.client.post(url_for('/post/roundstrength'), json={"buystrength" : "50", "stratstrength" : '50'})
        print(response)
        self.assertIn(b'Your power-level is 50%', response.data)

    def test_roundstrength2(self):
        response = self.client.post(url_for('/post/roundstrength'), json={"buystrength" : "50", "stratstrength" : '100'})
        print(response)
        self.assertIn(b'Your power-level is 75%', response.data)