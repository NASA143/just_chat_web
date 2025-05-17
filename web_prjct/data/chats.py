# Файл создания таблицы

import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin



class Chats(SqlAlchemyBase, UserMixin, SerializerMixin):
    # Имя таблицы
    __tablename__ = 'chats'

    # id сообщения
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    # Отправитель
    id_user_from = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    # Получатель
    id_user_to = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    # Текст сообщения
    msg = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # Время отправки
    created_time = sqlalchemy.Column(sqlalchemy.BLOB, default=datetime.datetime.now)
