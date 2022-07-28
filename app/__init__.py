from flask import Flask,render_template,redirect,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import psycopg2

import logging


app = Flask(__name__)

app.config['SECRET_KEY'] = '01fcfdbeca8650acf466a53d4b45f24e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://updljteaflhium:c0151e04752741e92119e1dc3c19132eaabe91ae3332085c0459d4dbae9b743e@ec2-44-208-88-195.compute-1.amazonaws.com:5432/d462304k9n45sm'
db = SQLAlchemy(app)
migrate  = Migrate(app,db)

# 

app.logger.setLevel(logging.ERROR)

from app import views