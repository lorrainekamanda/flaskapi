#!/usr/bin/python3
import secrets
import os
import os.path as op
from flask import Flask,render_template,redirect,url_for,request,jsonify,Response,make_response,url_for
from app import app,db
from app.models import Car
from app.forms import Form
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask_admin import Admin,form
from flask_admin.contrib.sqla import ModelView
from  markupsafe import Markup

ma = Marshmallow(app)
CORS(app)

admin = Admin(app,template_mode='bootstrap4')



@app.route('/')
def index():
    
    posts = Car.query.all()
    return render_template('home.html',posts=posts) 



    
# Image url
file_path = op.join(op.dirname(__file__), 'static/img')
try:
    os.mkdir(file_path)
except OSError:
    pass  

    
class ImageView(ModelView):
    
    # Add ImageUpload field to Admin .
    
    form_extra_fields = {
        'image_file': form.ImageUploadField('Car',
                                      base_path=file_path,
                                      thumbnail_size=(100, 100, True))
    }

admin.add_view(ImageView(Car, db.session))


# creating serialized api data        
class CarSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Car
        fields = ('id','name','gearbox','brand','price','fuel','motor','register','image_file')

car_schema = CarSchema()
cars_schema = CarSchema(many=True)
 
@app.route('/api',methods = ['GET'])
def get():
    cars = db.session.query(Car).all()
    results = cars_schema.dump(cars)
    
    return (jsonify(results))

        

if __name__ == '__main__': 
    app.run(debug=True)