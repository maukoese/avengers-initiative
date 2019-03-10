from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from ..models import Department, Power

class DepartmentForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class PowerForm(FlaskForm):
    """
    Form for admin to add or edit a power
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AvengerAssignForm(FlaskForm):
    """
    Form for admin to assign departments and powers to avengers
    """
    department = QuerySelectField(query_factory=lambda: Department.query.all(),
                                  get_label="name")
    power = QuerySelectField(query_factory=lambda: Power.query.all(),
                            get_label="name")
    submit = SubmitField('Submit')