from flask import Flask,render_template,redirect,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import psycopg2
from flask_heroku import Heroku


app = Flask(__name__)

app.config['SECRET_KEY'] = '01fcfdbeca8650acf466a53d4b45f24e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://lorrainekamanda:leilanjeri@localhost/car'
db = SQLAlchemy(app)
migrate  = Migrate(app,db)
heroku = Heroku(app)

from app import views