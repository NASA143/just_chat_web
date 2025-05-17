from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_rep = PasswordField('Повторите пароль', validators=[DataRequired()])

    submit = SubmitField('Зерегистрироваться')