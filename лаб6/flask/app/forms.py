from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class InsertClubForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    rating = StringField('Рейтинг', validators=[DataRequired()])
    confederacy_id = StringField('Конфедерация', validators=[DataRequired()])
    sponsor_id = StringField('Спонсор', validators=[DataRequired()])
    submit = SubmitField('Добавить')

class InsertConfederacyForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    submit = SubmitField('Добавить')
