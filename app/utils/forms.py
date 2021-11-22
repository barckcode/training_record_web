from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, validators

class ContactForm(FlaskForm):
    id_telegram = StringField("ID Telegram",  [validators.DataRequired("Por favor, introduce el ID de Telegram.")])
    name = StringField("Name",  [validators.DataRequired("Por favor, introduce el nombre del ejercicio.")])
    weight = StringField("Weight")
    repetitions = StringField("Repetitions")
    date = DateField("DatePicker",  format='%Y-%m-%d')
    submit = SubmitField("Send")
