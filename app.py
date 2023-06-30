from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:0000@localhost/testflask'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About page'

@app.route('/hello', methods=["GET", "POST"])
@app.route('/hello/<name>')
def hello(name=None):
    if request.method == 'POST':
        name = request.form.get('name')
        print('name: ', name)
        new_user = Test(name=name)
        db.session.add(new_user)
        db.session.commit()

    return render_template('index.html', name=name)
