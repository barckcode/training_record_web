from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, validators

class ContactForm(FlaskForm):
    id_telegram = StringField("ID Telegram",  [validators.DataRequired("Por favor, introduce el ID de Telegram.")])
    name = StringField("Nombre del Ejercicio",  [validators.DataRequired("Por favor, introduce el nombre del ejercicio.")])
    weight = StringField("Peso")
    repetitions = StringField("Nº Repeticiones")
    date = DateField("Fecha",  format='%Y-%m-%d')
    submit = SubmitField("Send")
