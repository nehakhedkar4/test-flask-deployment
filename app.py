from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About page'

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)