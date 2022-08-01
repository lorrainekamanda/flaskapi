from app import db
import sqlalchemy_utils
from sqlalchemy_utils.types.choice import ChoiceType

# database schema
class Car(db.Model):
    BRAND_TYPES = [
         ('mercedes', 'Mercedes'),
         ('bmw', 'BMW'),
         ('rangerrover', 'Range Rover'),
         ('vox', 'VoxWagen'),
         ('Other', 'Other')
    ]

    FUEL_TYPES = [
         ('diesel', 'Diesel'),
         ('petrol', 'Petrol'),
         ('electric', 'Electric'),
        
     ]
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(20),unique = True,nullable = False)
    price = db.Column(db.Integer)
    fuel = db.Column(ChoiceType(FUEL_TYPES))
    motor = db.Column(db.String(50))
    register = db.Column(db.String(50))
    brand  = db.Column(ChoiceType(BRAND_TYPES))
    gearbox = db.Column(db.String(50))
    image_file = db.Column(db.String(120),unique = True)


    
    def __repr__(self):
        return f"{self.name}"

    def __init__(self,name,price,image_file,fuel,motor,register,brand,gearbox):
        self.name = name
        self.price = price
        self.fuel = fuel
        self.motor = motor
        self.register = register
        self.brand = brand
        self.image_file = image_file




