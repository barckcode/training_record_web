import os
from flask import Flask, render_template, request, flash

# Internal modules
from utils import ContactForm, send_message


app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/', methods=['GET', 'POST'])
def home_page():
    form = ContactForm()

    if request.method == 'POST':
        # if form.validate() == False:
        #     flash('El correo indicado no es válido.')
        #     return render_template('home.html.j2', form=form)
        # else:
        id_telegram = str(form.id_telegram.data)
        name = str(form.name.data)
        weight_01 = str(form.weight_01.data)
        repetitions_01 = str(form.repetitions_01.data)
        weight_02 = str(form.weight_02.data)
        repetitions_02 = str(form.repetitions_02.data)
        weight_03 = str(form.weight_03.data)
        repetitions_03 = str(form.repetitions_03.data)
        weight_04 = str(form.weight_04.data)
        repetitions_04 = str(form.repetitions_04.data)
        date = str(form.date.data)

        resp = send_message(
            id_telegram,
            name,
            weight_01,
            weight_02,
            weight_03,
            weight_04,
            repetitions_01,
            repetitions_02,
            repetitions_03,
            repetitions_04,
            date
        )
        flash(resp)
        return render_template('home.html.j2', form=form)

    elif request.method == 'GET':
        return render_template('home.html.j2', form=form)

    return render_template(
        'home.html.j2',
        title = "TrainingRecord",
        presentation = "Soy TrainingRecord, el bot que te ayudará a llevar un registro de todos tus entrenamientos.",
        form=form,
    )
