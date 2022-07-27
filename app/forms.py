from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,IntegerField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed,FileField

class Form(FlaskForm):
    name = StringField('Name of the car',
                        validators=[DataRequired()])
    
    price = IntegerField('Price')
    image_file = FileField('Choose Photo',validators = [FileAllowed(['jpg','jpeg','png'])])
    submit = SubmitField('upload')