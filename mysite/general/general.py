from flask import Blueprint, render_template
from flask_login import current_user, login_required
import datetime

general_blueprint = Blueprint('general', __name__, 
   template_folder='templates', static_folder='static')

@general_blueprint.route("/")
@general_blueprint.route("/index")
def index():
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    content_variable = {'date': current_date}
    return render_template('general/index.html', **content_variable)

@general_blueprint.route("/portfolio")
@login_required
def portfolio():
    full_name = current_user.first_name + ' ' + current_user.last_name
    return render_template('general/portfolio.html', full_name=full_name)