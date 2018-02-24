from flask import Flask
from flask import jsonify
from flask import request
from mongoengine import *
connect('mongoengine_test', host='localhost', port=27017)

app = Flask(__name__)

class User(Document):
    name = StringField(required=True, max_length=200)

@app.route("/")
def hello():
    post_1 = User(
    name='Ali'
    )
    post_1.save()
    print(post_1.name)
    return "Hello World!"
#first commen
