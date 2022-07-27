from app import db



class Car(db.Model):

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(20),unique = True,nullable = False)
    price = db.Column(db.Integer)
    fuel = db.Column(db.String(50))
    motor = db.Column(db.String(50))
    register = db.Column(db.String(50))
    brand  = db.Column(db.String(50))
    gearbox = db.Column(db.String(50))
    image_file = db.Column(db.String(20),unique = True)
    
    def __repr__(self):
        return f"{self.name} {self.description}  {self.price} ({self.image_file})"

    def __init__(self,name,price,description,image_file):
        self.name = name
        self.description = description
        self.price = price
        self.image_file = image_file




