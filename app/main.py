from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template(
        'home.html.j2',
        title = "TrainingRecord",
        presentation = "Soy TrainingRecord, el bot que te ayudará a llevar un registro de todos tus entrenamientos.",
    )
