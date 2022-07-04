from flask import Flask,make_response,request,jsonify
from flask_mongoengine import MongoEngine
import urllib

from requests import request
app=Flask(__name__)
database_name='API'
mongodb_password=urllib.parse.quote_plus('Vikash@987')
DB_URI='mongodb+srv://vkvikashkumar987:{}@pycluster.uvhan.mongodb.net/API?retryWrites=true&w=majority'.format(mongodb_password)
app.config['MONGODB_HOST']=DB_URI
db=MongoEngine()
db.init_app(app)