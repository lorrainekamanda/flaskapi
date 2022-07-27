#!/usr/bin/python3
import secrets
import os
from flask import Flask,render_template,redirect,url_for,request,jsonify,Response
from app import app,db
from app.models import Car
from app.forms import Form
from flask_marshmallow import Marshmallow
from flask_cors import CORS

ma = Marshmallow(app)
CORS(app)

@app.route('/')
def index():
    
    posts = Car.query.all()
    return render_template('home.html',posts=posts) 


def upload_pic(save_picture):
    random_hex = secrets.token_hex(8)
    _,f_ext = os.path.splitext(save_picture.filename)

    picture_name = random_hex + f_ext
    load = os.path.join(app.root_path,'static/img/',picture_name)

    save_picture.save(load)
    return picture_name


@app.route('/form',methods = ['GET','POST'])

def submit():
        form = Form()
        
        if form.validate_on_submit():
            picture_path = upload_pic(form.image_file.data)
            
            car = Car(name = form.name.data,image_file = picture_path)
            db.session.add(car)
            db.session.commit()     
            return redirect(url_for('index'))

        
        picture = url_for('static',filename=('img/'+image_file),code = 301)
       

        return render_template('form.html', title='Form', form=form,picture=picture)

class CarSchema(ma.Schema):
    class Meta:
        fields = ('id','name','image_file')

car_schema = CarSchema()
cars_schema = CarSchema(many=True)
 
@app.route('/api',methods = ['GET'])
def books():
    cars = Car.query.all()
    results = cars_schema.dump(cars)
    
    return jsonify(results)

        

if __name__ == '__main__': 
    app.run(debug=True)