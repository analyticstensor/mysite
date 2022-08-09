from threading import Thread
from flask import Blueprint, current_app, render_template
from flask_mail import Mail, Message


email_blueprint = Blueprint('email', __name__, template_folder='templates')

mail = Mail()

def send_async_email(app, message):
    with app.app_context():
        mail.send(message)

def send_email(subject, sender, receipients, text_body, html_body, attachment=None, sync=False):
    message = Message(subject, sender=sender, recipients=receipients)
    message.body = text_body
    message.html = html_body
    if attachment:
        for atch in attachment:
            message.attach(*atch)
    if sync:
        mail.send(message)
    else:
        Thread(target=send_async_email, args=(current_app._get_current_object(), message)).start()

def send_forget_password_email(user):
    token = user.get_forget_password_token()
    send_email('Password Reset Notification', sender=current_app.config['MAIL_SENDER'], receipients=[user.email],
               text_body="", #render_template('email/reset_password_notification.txt', user=user, token=token),
               html_body=render_template('email/reset_password_notification_email.html', user=user, token=token))

def send_reset_password_email(user):
    send_email('Password Changed Notification', sender=current_app.config['MAIL_SENDER'], receipients=[user.email],
               text_body="",
               html_body=render_template('email/reset_password_success_email.html', user=user))