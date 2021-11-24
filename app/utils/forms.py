from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, validators

class ContactForm(FlaskForm):
    id_telegram = StringField("ID Telegram",  [validators.DataRequired("Por favor, introduce el ID de Telegram.")])
    name = StringField("Nombre del Ejercicio",  [validators.DataRequired("Por favor, introduce el nombre del ejercicio.")])
    weight_01 = StringField("Peso (Kg)")
    repetitions_01 = StringField("Nº Repeticiones")
    weight_02 = StringField("Peso (Kg)")
    repetitions_02 = StringField("Nº Repeticiones")
    weight_03 = StringField("Peso (Kg)")
    repetitions_03 = StringField("Nº Repeticiones")
    weight_04 = StringField("Peso (Kg)")
    repetitions_04 = StringField("Nº Repeticiones")
    date = DateField("Fecha",  format='%Y-%m-%d')
    submit = SubmitField("Send")
