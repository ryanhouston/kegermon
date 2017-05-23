from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class TapUpdateForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    style = StringField('Style', validators=[DataRequired()])
    description = TextAreaField('Description')
    position = SelectField('Tap Position',
                           coerce=int,
                           choices=[(1,1), (2,2), (3,3), (4,4)],
                           validators=[DataRequired()])
