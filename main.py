from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')


db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db.init_app(app)
app.config.from_pyfile('config.py')


@app.route('/')
def home():
    return '<h1>Welcome Flask application Home</h1>'


@app.route('/<name>')
def hello_world(name):
    return f'<h1>Hello {name}</h1>'


if __name__ == '__main__':
    app.run()
