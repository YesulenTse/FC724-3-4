from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, RadioField
from wtforms.validators import InputRequired


class Questionnaire(FlaskForm):
    name = StringField('name', validators=[InputRequired()])
    course = StringField('course', validators=[InputRequired()])
    short_answer = TextAreaField('short-answer', validators=[InputRequired()])
    long_answer = TextAreaField('long-answer', validators=[InputRequired()])
    satisfaction = SelectField('Overall Satisfaction', choices=[
        ('', 'Select Satisfaction Level'),
        ('very-satisfied', 'Very Satisfied'),
        ('satisfied', 'Satisfied'),
        ('neutral', 'Neutral'),
        ('unsatisfied', 'Unsatisfied'),
        ('very-unsatisfied', 'Very Unsatisfied')
    ], validators=[InputRequired()])
    recommend = RadioField('Would you recommend this course to others?', choices=[
        ('yes', 'Yes'),
        ('no', 'No')
    ], validators=[InputRequired()])
    improvements = TextAreaField('Suggestions for Improvement', validators=[InputRequired()])
