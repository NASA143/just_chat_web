# Файл создания таблицы

import sqlalchemy
from .db_session import SqlAlchemyBase
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    # Имя таблицы
    __tablename__ = 'users_tab'

    # id пользователя
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    # Логин пользователя
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # Пароль
    password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    #  Имеющиеся чаты с пользователями
    chats_with = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # Изображение пользователя
    image = sqlalchemy.Column(sqlalchemy.BLOB, nullable=True)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
