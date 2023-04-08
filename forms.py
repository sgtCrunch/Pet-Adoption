from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, ValidationError, RadioField, SelectField
from wtforms.validators import InputRequired, Optional, AnyOf, URL, StopValidation

def valid_age(form, field):
    if 0 < field.data > 31:
        raise ValidationError('Age must be between 1 and 30')

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Name",
                            validators=[InputRequired()])
    species = SelectField("Species",
                            choices=[('dog', 'Dog'), ("Porcupine", 'Porcupine'), ('Cat', 'Cat')],
                            validators=[InputRequired()])
    photo_url = StringField("Img URL",
                            validators=[Optional(), URL()])
    age = IntegerField("Age",
                            validators=[Optional(), valid_age])
    notes = TextAreaField("Notes",
                            validators=[Optional()])
    

class EditPetForm(FlaskForm):
    """Form for editing pets."""

    photo_url = StringField("Img URL",
                            validators=[Optional(), URL()])
    notes = TextAreaField("Notes",
                            validators=[Optional()])
    available = SelectField('Available',
                        choices=[(1, 'Available'), (0, 'Not Available')],
                        coerce=int,
                        validators=[InputRequired()])