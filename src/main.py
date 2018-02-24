from flask import Flask
from flask import jsonify
from flask import request
from mongoengine import *
connect('mongoengine_test', host='localhost', port=27017)

app = Flask(__name__)

class User(Document):
    username = StringField(required=True, max_length=200)

@app.route("/")
def hello():
    return "Hello World!"
#first commen
