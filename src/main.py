from flask import Flask, render_template, url_for
from flask import jsonify
from flask import request
from mongoengine import *
connect('mongoengine_test', host='localhost', port=27017)

app = Flask(__name__)

class User(Document):
    username = StringField(required=True, max_length=200)
    password = StringField(required=True, max_length=200)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        return 'Hello World'
