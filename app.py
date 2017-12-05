from flask import  Flask,render_template,flash, redirect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost/Resources'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config.update(SECRET_KEY = 'TresTristresTigres')

db = SQLAlchemy(app)
Bootstrap(app)

# app.config.from_object('config')


# class Request(db.Model):
# 	__tablename__ = 'request'

# 	id = db.Column(db.Integer, primary_key=True)
# 	p_id = db.Column(db.Integer)
# 	r_id = db.Column(db.Integer)
# 	qty_request = db.Column(db.Integer)


# 	def __init__(self, person_id, resource_id, quatity ):
# 		p_id = person_id
# 		r_id = resource_id
# 		qty_request = quatity




# # db.create_all()

# # db.session.add(User(456,234,10))
# # db.session.add(User(578,345,6))

# # db.session.commit()


@app.route('/')


def index():
	
	return  render_template('index.html');






@app.route('/login', methods=['GET','POST'])

def login():

	form = LoginForm()

	if form.validate_on_submit():
		flash('Login Requested for User= "%s", Password= "%s", remember_me="%s" ' %  (form.user.data, form.pswd.data, str(form.remember_me.data)))
		return redirect('/')
	
	return render_template('login.html',
							title = 'Sign In',
							form=form)


if __name__ ==  "__main__":
	app.run(debug = True)