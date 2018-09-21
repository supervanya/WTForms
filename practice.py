from flask import Flask, request, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Required

import requests
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.debug = True

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    age = IntegerField('What is your age?', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/')
def home():
    return "Hello, world!"

@app.route('/index')
def index():
    simpleForm = NameForm()
    return render_template('practice-form.html', form=simpleForm)

@app.route('/result', methods = ['GET', 'POST'])
def result():
    form = NameForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        name = form.name.data
        age = form.age.data
        return "Your name is {0} and your age is {1}".format(name,age)
    flash('Fill everything in correctly!')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
