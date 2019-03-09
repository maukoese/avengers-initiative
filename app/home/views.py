from flask import render_template
from flask_login import login_required

from . import home


@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")


@home.route('/mansion')
@login_required
def mansion():
    """
    Render the mansion template on the /mansion route
    """
    return render_template('home/mansion.html', title="Mansion")