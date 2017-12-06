from flask import  Flask,render_template,flash, redirect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from resource import ResourceHandler as RHandle
from request import RequestHandler as RQHandle


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost/Resources'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config.update(SECRET_KEY = 'TresTristresTigres')

db = SQLAlchemy(app)
Bootstrap(app)

# app.config.from_object('config')


class Request(db.Model):
	__tablename__ = 'request'

	id = db.Column(db.Integer, primary_key=True)
	p_id = db.Column(db.Integer)
	r_id = db.Column(db.Integer)
	qty_request = db.Column(db.Integer)


	def __init__(self, person_id, resource_id, quatity ):
		p_id = person_id
		r_id = resource_id
		qty_request = quatity





@app.route('/')

def index():
	
	return  render_template('index.html');

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
    	return 'dimelo pa';

@app.route('/show/users')

def showUsers():
    	return "This is the Table of Currets users";

@app.route('/show/admin')

def showAdministrators():
    	return "What how did you get here, this is for administrators only";

if __name__ ==  "__main__":
	app.run(debug = True)