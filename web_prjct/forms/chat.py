from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField, StringField
from wtforms.validators import DataRequired


class ChatForm(FlaskForm):
    msg = StringField('Сообщение', validators=[DataRequired()])
    send = SubmitField('Отправить')