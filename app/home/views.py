from flask import abort, render_template
from flask_login import current_user, login_required

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

@home.route('/mansion/admin_section')
@login_required
def admin_section():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)

    return render_template('home/admin_section.html', title="Mansion")