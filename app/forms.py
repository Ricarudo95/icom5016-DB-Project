
from flask_wtf import FlaskForm as Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import InputRequired

class LoginForm(Form):
	user = StringField('user', validators=[InputRequired()])
	pswd = PasswordField('pswd', validators=[InputRequired()])
	remember_me = BooleanField('remember_me', default=False)