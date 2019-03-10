from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from forms import DepartmentForm, AvengerAssignForm, PowerForm
from .. import db
from ..models import Avenger, Department, Power


def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)


# Department Views


@admin.route('/departments', methods=['GET', 'POST'])
@login_required
def list_departments():
    """
    List all departments
    """
    check_admin()

    departments = Department.query.all()

    return render_template('admin/departments/departments.html',
                           departments=departments, title="Departments")


@admin.route('/departments/add', methods=['GET', 'POST'])
@login_required
def add_department():
    """
    Add a department to the database
    """
    check_admin()

    add_department = True

    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(name=form.name.data,
                                description=form.description.data)
        try:
            # add department to the database
            db.session.add(department)
            db.session.commit()
            flash('You have successfully added a new department.')
        except:
            # in case department name already exists
            flash('Error: department name already exists.')

        # redirect to departments page
        return redirect(url_for('admin.list_departments'))

    # load department template
    return render_template('admin/departments/department.html', action="Add",
                           add_department=add_department, form=form,
                           title="Add Department")


@admin.route('/departments/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_department(id):
    """
    Edit a department
    """
    check_admin()

    add_department = False

    department = Department.query.get_or_404(id)
    form = DepartmentForm(obj=department)
    if form.validate_on_submit():
        department.name = form.name.data
        department.description = form.description.data
        db.session.commit()
        flash('You have successfully edited the department.')

        # redirect to the departments page
        return redirect(url_for('admin.list_departments'))

    form.description.data = department.description
    form.name.data = department.name
    return render_template('admin/departments/department.html', action="Edit",
                           add_department=add_department, form=form,
                           department=department, title="Edit Department")


@admin.route('/departments/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_department(id):
    """
    Delete a department from the database
    """
    check_admin()

    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    flash('You have successfully deleted the department.')

    # redirect to the departments page
    return redirect(url_for('admin.list_departments'))

    return render_template(title="Delete Department")



@admin.route('/powers')
@login_required
def list_powers():
    check_admin()
    """
    List all powers
    """
    powers = Power.query.all()
    return render_template('admin/powers/powers.html',
                           powers=powers, title='Powers')


@admin.route('/powers/add', methods=['GET', 'POST'])
@login_required
def add_power():
    """
    Add a power to the database
    """
    check_admin()

    add_power = True

    form = PowerForm()
    if form.validate_on_submit():
        power = Power(name=form.name.data,
                    description=form.description.data)

        try:
            # add power to the database
            db.session.add(power)
            db.session.commit()
            flash('You have successfully added a new power.')
        except:
            # in case power name already exists
            flash('Error: power name already exists.')

        # redirect to the powers page
        return redirect(url_for('admin.list_powers'))

    # load power template
    return render_template('admin/powers/power.html', add_power=add_power,
                           form=form, title='Add Power')


@admin.route('/powers/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_power(id):
    """
    Edit a power
    """
    check_admin()

    add_power = False

    power = Power.query.get_or_404(id)
    form = PowerForm(obj=power)
    if form.validate_on_submit():
        power.name = form.name.data
        power.description = form.description.data
        db.session.add(power)
        db.session.commit()
        flash('You have successfully edited the power.')

        # redirect to the powers page
        return redirect(url_for('admin.list_powers'))

    form.description.data = power.description
    form.name.data = power.name
    return render_template('admin/powers/power.html', add_power=add_power,
                           form=form, title="Edit Power")


@admin.route('/powers/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_power(id):
    """
    Delete a power from the database
    """
    check_admin()

    power = Power.query.get_or_404(id)
    db.session.delete(power)
    db.session.commit()
    flash('You have successfully deleted the power.')

    # redirect to the powers page
    return redirect(url_for('admin.list_powers'))

    return render_template(title="Delete Power")



@admin.route('/avengers')
@login_required
def list_avengers():
    """
    List all avengers
    """
    check_admin()

    avengers = Avenger.query.all()
    return render_template('admin/avengers/avengers.html',
                           avengers=avengers, title='Avengers')


@admin.route('/avengers/assign/<int:id>', methods=['GET', 'POST'])
@login_required
def assign_avenger(id):
    """
    Assign a department and a power to an avenger
    """
    check_admin()

    avenger = Avenger.query.get_or_404(id)

    # prevent admin from being assigned a department or power
    if avenger.is_admin:
        abort(403)

    form = AvengerAssignForm(obj=avenger)
    if form.validate_on_submit():
        avenger.department = form.department.data
        avenger.power = form.power.data
        db.session.add(avenger)
        db.session.commit()
        flash('You have successfully assigned a department and power.')

        # redirect to the powers page
        return redirect(url_for('admin.list_avengers'))

    return render_template('admin/avengers/avenger.html',
                           avenger=avenger, form=form,
                           title='Assign Avenger')