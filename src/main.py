from flask import Flask, render_template, url_for
from flask import jsonify
from flask import request
import googlemaps
from datetime import datetime
from mongoengine import *
connect('mongoengine_test', host='localhost', port=27017)

gmaps = googlemaps.Client(key='AIzaSyAO4q3ZkN0AOF1MK2Or2LitgcZJPzpBdQk')
now = datetime.now()
app = Flask(__name__)

class User(Document):
    username = StringField(required=True, max_length=200)
    password = StringField(required=True, max_length=200)
    email = StringField(required=True, max_length=200)
    interests = ListField(StringField(required=True, max_length=50))
    zipCode = StringField(required = True, max_length = 200)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        if 'email' in request.form:
            user = User(request.form['username'], request.form['password'], request.form['email'])
            user.save()
            return request.form['username']
        else:
            for user in User.objects:
                if user.password == request.form['password']:
                    return "Authenticated"
            return render_template("interests.html")
@app.route('/interests', methods=['GET', 'POST'])
def interests():
    if request.method == 'GET':
        return render_template("interests.html")
    else:
        return request.form
        arr = []
        for i in range(len(request.form)):
            arr.append(request.form[i])
        user = User.objects(username=request.args.get('username'))
        user.interests = arr

@app.route('/find', methods=['GET', 'POST'])
def find():
    pass

@app.route('/zipCode', methods=['GET','POST'])
def zipCode():
    if request.method == 'POST' and request.form['zipcode']:
        return redirect(url_for('zipCode'))
    elif request.args.get('confirm') == '1':
        return User(zipcode, self).post()
    else:
        return render_template('zipCode.html')

@app.route('/map', methods=['GET'])
def map():
    return render_template("map.html")
