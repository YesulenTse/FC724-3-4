from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired

class Questionnaire(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    student_number = StringField('Student Number', validators=[InputRequired()])
    programme_type = SelectField('Programme Type', choices=[
        ('undergraduate', 'Undergraduate'),
        ('postgraduate', 'Postgraduate')
    ], validators=[InputRequired()])
    grades = SelectField('Grades', choices=[
        ('90+', '90+'),
        ('80+', '80+'),
        ('70+', '70+'),
        ('60+', '60+'),
        ('other', 'Other')
    ], validators=[InputRequired()])
    satisfaction = SelectField('Overall Satisfaction', choices=[
        ('very-satisfied', 'Very Satisfied'),
        ('satisfied', 'Satisfied'),
        ('neutral', 'Neutral'),
        ('unsatisfied', 'Unsatisfied'),
        ('very-unsatisfied', 'Very Unsatisfied')
    ], validators=[InputRequired()])
    suggestions = TextAreaField('Suggestions')
