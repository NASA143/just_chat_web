import random
import datetime

from sqlalchemy import or_

from flask import Flask, render_template, redirect, request, make_response, session, abort, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from data import db_session
from data.users import User
from data.chats import Chats

from flask_login import LoginManager, login_user

from forms.chat import ChatForm
from forms.login import LoginForm
from forms.register import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(
    days=365
)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # Событие нажатия на кнопку
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.name == form.login.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect('/chats')

    return render_template('login.html', form=form)


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    form = RegisterForm()
    # Событие нажатия на кнопку
    if form.validate_on_submit():
        # Проверка совпадения паролей
        if form.password.data == form.password_rep.data and form.password != '':
            # Создание сессии БД
            db_sess = db_session.create_session()
            if db_sess.query(User).filter(User.name != form.login.data).first() or db_sess.query(User).filter(User.name != form.login.data).first() == None:
                user = User(
                    name=form.login.data,
                    chats_with="[]"
                )
                user.set_password(form.password.data)
                db_sess.add(user)
                db_sess.commit()
    return render_template('reg.html', form=form)

@app.route('/chats', methods=['GET', 'POST'])
def chats():
    form = ChatForm()
    chat_list = eval(current_user.chats_with)
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'press':
            active_chat = 2
            db_sess = db_session.create_session()
            data = db_sess.query(Chats).filter(or_(Chats.id_user_to == active_chat, Chats.id_user_from == 1))
            print(data[0].msg)
            return render_template('chat.html', user_id=1, chat_list=chat_list, form=form, msgs=data)

    return render_template('chat.html', chat_list=chat_list, form=form)

def main():
    db_session.global_init("db/main.db")
    app.run(host="0.0.0.0", port=8143)


if __name__ == '__main__':
    main()