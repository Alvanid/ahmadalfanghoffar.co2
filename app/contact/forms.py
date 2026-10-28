from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField('Nama Lengkap', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    subject = StringField('Subjek', validators=[DataRequired(), Length(min=5, max=150)])
    message = TextAreaField('Pesan', validators=[DataRequired(), Length(min=10, max=1000)])
    submit = SubmitField('Kirim Pesan')