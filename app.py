from flask import  Flask, jsonify, request
from resource import ResourceHandler as RHandle
from request import RequestHandler as RQHandle

app = Flask(__name__)


@app.route('/')

def index():
	return 'Disaster Site!'

@app.route('/test')

def test():
	return "Como poco coco come poco coco compra"


@app.route('/show/request')

def showRequest():
    	return RQHandle().getAllRequest();

@app.route('/show/resources')
def showResources():
<<<<<<< HEAD
=======

>>>>>>> 83a2177dd228bae29186552f006b24d8c97b498a
    	return RHandle().getAllResources();

@app.route('/show/resource/<int:rid>')
def getResources(rid):
    	return RHandle().getResourceById(rid);
<<<<<<< HEAD
=======



>>>>>>> 83a2177dd228bae29186552f006b24d8c97b498a

@app.route('/show/supplier')

def showSupplier():
    	return 'dimelo pa';

@app.route('/show/users')

def showUsers():
    	return "This is the Table of Currets users";

@app.route('/show/admin')

def showAdministrators():
    	return "What how did you get here, this is for administrators only";

if __name__ ==  "__main__":
	app.run(debug = True)
