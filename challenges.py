#import statements go here
from flask import Flask, request, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Required, Email

import requests
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.debug = True

class itunesForm(FlaskForm):
    # Artist name - required field
    name = StringField("Artist's Name",validators=[Required()])
    # Number of results iTunes API should return - required field
    results_number = IntegerField("Number of results?",validators=[Required()])
    # User’s email - required field, should be validated  (HINT : Refer to WTForms Documentation to identify validators)
    email = StringField("Your email?", validators=[Required(),Email()])
    # Submit button
    submit = SubmitField('Submit')


@app.route('/')
def home():
    return "Hello, world!"

#create class to represent WTForm that inherits flask form

@app.route('/itunes-form', methods = ['GET', 'POST'])
def itunes_form():
    itunes_form = itunesForm()
    return render_template('itunes-form.html', form=itunes_form) # HINT : create itunes-form.html to represent the form defined in your class

@app.route('/itunes-result', methods = ['GET', 'POST'])
def itunes_result():
    itunes_form = itunesForm(request.form)

    if request.method == "POST": # itunes_form.validate_on_submit():


        name    = itunes_form.name.data
        n       = itunes_form.results_number.data
        email   = itunes_form.email.data

        # return (name+str(n)+str(email))


        params      = { "term":  name,
                        "media": 'music',
                        "limit": n
                        }

        baseurl         = "https://itunes.apple.com/search"
        response        = requests.get(baseurl, params = params)
        response_json   = response.json()

        # print(response.url)
        # print(response_json)

        return render_template('itunes-form.html', form=itunes_form) + render_template('itunes-result.html', form=itunes_form, results = response_json["results"])



    #what code goes here?
    # HINT : create itunes-results.html to represent the results and return it
    flash('All fields are required!')
    return("didn't work") # TODO remove
    return redirect(url_for('itunes_form')) #this redirects you to itunes_form if there are errors

if __name__ == '__main__':
    app.run()
