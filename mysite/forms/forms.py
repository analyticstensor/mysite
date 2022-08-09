from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, validators
from wtforms.validators import DataRequired, Email, EqualTo

textbox_style = {'class':'input is-large', 'autofocus':'true'}
submit_style = {'class':'button is-block is-info is-large is-fullwidth'}

class SignUpForm(FlaskForm):
    """
    User Sign Up Form
    """
    first_name = StringField('First Name', [DataRequired(), validators.Length(min=2, max=20)], description={'placeholder': 'First Name'}, render_kw=textbox_style)
    last_name = StringField('Last Name', [DataRequired(), validators.Length(min=2, max=20)], render_kw=textbox_style)
    email = StringField('Email', [Email(message=('Please enter valid email')), DataRequired()], render_kw=textbox_style)
    password = PasswordField('Password', [DataRequired()], render_kw=textbox_style)
    confirm_password = PasswordField('Confirm Password', [DataRequired(), EqualTo('password', message='Password doesn\'t match.')], render_kw=textbox_style)
    submit = SubmitField('Submit', render_kw=submit_style)

class LoginForm(FlaskForm):
    """
    User Login Form
    """
    email = StringField('Email', [Email(message=('Please enter valid email')), DataRequired()], render_kw=textbox_style)
    password = PasswordField('Password', [DataRequired()], render_kw=textbox_style)
    remember = BooleanField('Remember me')
    submit = SubmitField('Submit', render_kw=submit_style)

class ForgetPasswordRequestForm(FlaskForm):
    """
    Forget Password Request Form
    """
    email = StringField('Email', [Email(message=('Please enter valid email')), DataRequired()], render_kw=textbox_style)
    submit = SubmitField('Forget Password', render_kw=submit_style)

class ResetPasswordForm(FlaskForm):
    """
    Reset Password Form
    """
    password = PasswordField('New Password', [DataRequired()], render_kw=textbox_style)
    confirm_password = PasswordField('Confirm New Password', [DataRequired(), EqualTo('password', message='Password doesn\'t match.')], render_kw=textbox_style)
    submit = SubmitField('Reset Password', render_kw=submit_style)
