from flask import  Flask, jsonify, request
from resource import ResourceHandler as RHandle
from request import RequestHandler as RQHandle
from supplier import SupplierHandler as SHandler
from user import UserHandler as UHandler
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

@app.route('/show/resource')
def showResources():
    	return RHandle().getAllResources();

@app.route('/show/resource/<int:rid>')
def getResources(rid):
    	return RHandle().getResourceById(rid);

@app.route('/show/supplier')
def showSupplier():
    	return SHandler().getAllSupplier();

@app.route('/show/users')

def showUsers():
    	return UHandler().getAllUser();

@app.route('/show/admin')

def showAdministrators():
    	return "What how did you get here, this is for administrators only";

if __name__ ==  "__main__":
	app.run(debug = True)
