from app_files import app
from app_files.forms import SearchForm
from app_files.ai_model import Pipeline
from flask import render_template, redirect, url_for, flash, request 
import requests

pipe = Pipeline()

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = SearchForm()
    waitOver = False
    if form.validate_on_submit():
        query = str(form.search.data)
        results = pipe.predict(query)
        if len(results) > 0:
            waitOver = True
            return render_template('home.html', form = form, display = results, wait = waitOver)
    return render_template('home.html', form = form, display = None, wait = waitOver)