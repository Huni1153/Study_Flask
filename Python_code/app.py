import os
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

#현재 파일이 실행되는 경로
basedir = os.path.abspath(os.path.dirname(__file__))

# db파일이 저장되어있는 경로
dbfile = os.path.join(basedir,"db.sqlite")

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Test(db.Model):
    __tablename__ = 'test_table'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32), unique = True)

db.create_all()

@app.route('/')

def hello():
    return "Hello flask server"