import click
from flask import Flask
from flask_login import LoginManager
from mysite.models.models import db
from mysite.email.email import mail


def create_app():
    """
    Create app Object.
    """
    app = Flask(__name__, instance_relative_config=True)
      
    # App config
    app.config.from_object('config.Config')
  
    db.init_app(app)
    mail.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'authenticate.login'
    login_manager.init_app(app)

    from mysite.models.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from mysite.authenticate.authenticate import authenticate_blueprint
    from mysite.general.general import general_blueprint
    from mysite.email.email import email_blueprint

    # Register blueprint
    app.register_blueprint(authenticate_blueprint, url_prefix='/authenticate')
    app.register_blueprint(general_blueprint)
    app.register_blueprint(email_blueprint)
    
    # Add init-db command.
    @app.cli.command('init-db')
    def initialize_db():
        """
        Initialize database and create all tables.
        """
        click.echo("Creating tables.")
        db.create_all()

    return app

