from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo

class SignupForm(FlaskForm):
    full_name = StringField("Full Name", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField("SignUp")


class LoginForm(FlaskForm):
    email = StringField("Email:" , validators=[InputRequired(), Email()])
    password = PasswordField("Password:", validators=[InputRequired()])
    submit = SubmitField("Login")


class EditPetForm(FlaskForm):
    name = StringField("Pet's Name", validators = [InputRequired()])
    age = StringField("Pet's Age", validators = [InputRequired()])
    bio = StringField("Pet's Bio", validators = [InputRequired()])
    submit = SubmitField("Edit Pet")
    