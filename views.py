from flask import render_template

from simpleFlask import app

@app.route('/')
def index('/'):
    return render_template("index.html")

@app.route('/about')
def about():
    render_template('about.html')
