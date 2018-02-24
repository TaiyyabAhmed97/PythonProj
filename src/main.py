from flask import Flask
from flask import jsonify
from flask import request
from mongoengine import *
connect('mongoengine_test', host='localhost', port=27017)

app = Flask(__name__)

class User(Document):
    username = StringField(required=True, max_length=200)
    password = StringField(required=True, max_length=200)

@app.route('/login', methods=['POST'])
def login():
    person = User()
    person.save()
    print(person.name)
<<<<<<< HEAD
    return render_template('interests.html', error=error)
=======
    return render_template('login.html', error=error)
@app.route('/interests/<id>', methods=['POST'])
def interests():
    
>>>>>>> 8a5dbfc58eea3ad71d42ebab9cbfed9283dbcba3
