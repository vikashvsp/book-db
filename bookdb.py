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

class Book(db.Document):
    book_id=db.IntField()
    name=db.StringField()
    author=db.StringField()

    def to_json(self):
        return {
            "book_id": self.book_id,
            "name":self.name,
            "author":self.author
        }
@app.route('/api/createBook',methods=['POST'])
def db_populate():
    book1=Book(book_id=1,name='Ulysses',author='James Joyce')
    book2=Book(book_id=2,name='Don Quixote',author='Miguel de Cervantes')
    book1.save()
    book2.save()
    return make_response("",201)


@app.route('/api/books',methods=['GET','POST'])
def api_books():

    if request.method == "GET":
        books=[]
        for book in Book.objects:
            books.append(book)
        return make_response(jsonify(books),200)
    elif request.method=='POST':
        content=request.json
        book=Book(book_id=content['book_id'],name=content['name'],author=content['author'])
        book.save()
        return make_response("",201)