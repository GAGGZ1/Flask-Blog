from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] ='cc1954a0b2fa7878e90d95eb1bfbcae8'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db'
db=SQLAlchemy(app)

from flaskblog import routes