
from flask_wtf import FlaskForm as Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(Form):
	user = StringField('user', validators=[DataRequired()])
	pswd = PasswordField('pswd', validators=[DataRequired()])
	remember_me = BooleanField('remember_me', default=False)