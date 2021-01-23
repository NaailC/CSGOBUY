from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'
app.config["SECRET_KEY"]= 'sfdhjsagdsag'
db = SQLAlchemy(app)


from application import routes


