from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember")
    submit = SubmitField("Login")
    
    
class NewPost(FlaskForm):
    title = StringField("Title", validators =[DataRequired(), Length(min=5, max =22)])
    image = FileField("Image", validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    content =TextAreaField("Content", validators =[DataRequired()])
    submit =SubmitField("Submit")
    
class ContactForm(FlaskForm):
    name = StringField("Name")
    email = StringField("Email")
    subject = StringField("Subject")
    message = TextAreaField("Message")
    submit = SubmitField("Send")
    
    
