from File_editor.models import User,File
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from flask_login import current_user


# from wtforms.validators import

class LoginForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Login")


class CreateUser(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    fullname = StringField(label='Fullname', validators=[DataRequired()])
    Password = PasswordField(label="Password")
    confirm_password = PasswordField(label="Confirm Password", validators=[DataRequired(), EqualTo('Password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        print(user)
        if user:
            raise ValidationError("username exists")


class CreateFile(FlaskForm):
    filename = StringField(label="File Name:", validators=[DataRequired()])
    password = PasswordField(label="File Password", validators=[DataRequired()])
    confirm_password = PasswordField(label="Confirm File Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Create")
    
    def validate_filename(self, filename):
        file = File.query.filter_by(filename=filename.data, author=current_user).first()
        if file:
            raise ValidationError("filename exists")


class TextArea(FlaskForm):
    text = TextAreaField(label="text")
    rename = StringField(label="rename", validators=[DataRequired()])
    save = SubmitField("Save")
