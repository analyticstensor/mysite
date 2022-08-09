"""
User Authentication routes.
"""

from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, login_required, logout_user
from mysite.models.models import User
from mysite import db
from mysite.forms.forms import SignUpForm, LoginForm, ForgetPasswordRequestForm, ResetPasswordForm
from mysite.email.email import send_forget_password_email, send_reset_password_email

authenticate_blueprint =  Blueprint('authenticate', __name__, template_folder='templates')

@authenticate_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('general.portfolio'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            flash('Email doesn\'t exist.', 'error')
        elif user and not check_password_hash(user.password, form.password.data):
            flash('Password doesn\'t match.', 'warning')
        else:
            login_user(user, remember=form.remember.data)
            return redirect(url_for('general.portfolio'))
    return render_template('authenticate/login.html', login_form=form)

@authenticate_blueprint.route("/logout")
@login_required
def logout():
    # Update last_login
    current_user.update_last_login()
    logout_user()
    return redirect(url_for('general.index'))

@authenticate_blueprint.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        email_filter = User.query.filter_by(email=form.email.data).first()
        if email_filter:
            flash('User already exist.')
            return redirect(url_for('authenticate.signup'))
        else:
            user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data)
            user.hash_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('You have been registered.', 'success')
            return redirect(url_for('authenticate.login'))
    return render_template('authenticate/signup.html', signup_form=form)

@authenticate_blueprint.route("/forget_password_request", methods=['GET', 'POST'])
def forget_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('general.portfolio'))
    form = ForgetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash('Check your email to reset password.', 'success')
            send_forget_password_email(user)
            return render_template('email/reset_password_notification_display.html', user=user)
        else:
            flash('Email doesn\'t exist.', 'error')
    return render_template('authenticate/forget_password_request.html', forget_password_request_form=form)

@authenticate_blueprint.route("/forget_password/<token>", methods=['GET', 'POST'])
def forget_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('general.portfolio'))
    user = User.verify_forget_password_token(token)
    if not user:
        return redirect(url_for('authenticate.login'))
    form = ResetPasswordForm()
    if form.validate_on_submit():        
        user.hash_password(form.password.data)
        db.session.commit()
        flash('Your password has been changed.', 'success')
        send_reset_password_email(user)
        return render_template('email/reset_password_success.html', user=user)
    return render_template('authenticate/reset_password.html', reset_password_form=form)
    