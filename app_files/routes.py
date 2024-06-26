from app_files import app, db
from app_files.models import URL_Yelp
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

    recents = URL_Yelp.query.order_by(URL_Yelp.polarity.desc()).limit(5).all()
    url_list = [str(recent.url) for recent in recents]

    if form.validate_on_submit():
        query = str(form.search.data)
        results = pipe.predict(query)
        if len(results) > 0:
            waitOver = True
            return render_template('home.html', form = form, display = results, wait = waitOver, urls = url_list)
    return render_template('home.html', form = form, display = None, wait = waitOver, urls = url_list)