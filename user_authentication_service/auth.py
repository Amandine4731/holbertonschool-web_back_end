#!/usr/bin/env python3
"""
AUTH file
"""
import bcrypt
from db import DB
from user import User
import sqlalchemy
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
import uuid


def _hash_password(password: str) -> bytes:
    """ hash password for security """
    return bcrypt.hashpw(password.encode("UTF-8"), bcrypt.gensalt())


def _generate_uuid() -> str:
    """ generate uuid """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ register user """
        try:
            self._db.find_user_by(email=email)

            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            hash_pwd = _hash_password(password)
            return self._db.add_user(email=email, hashed_password=hash_pwd)

    def valid_login(self, email: str, password: str) -> bool:
        """ check is valid login """
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode("utf-8"),
                              user.hashed_password):
                return True
            else:
                return False
        except NoResultFound:
            return False

    def create_session(self, email) -> str:
        """ create session """
        try:
            user = self._db.find_user_by(email=email)
            user.session_id = _generate_uuid()
            self._db._session.commit()
            return user.session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """ find user by session_id """
        try:
            if session_id is None:
                return None
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ destroy session id """
        try:
            self._db.update_user(user_id, session_id=None)
        except InvalidRequestError:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """ create a token for reset the password """
        try:
            user = self._db.find_user_by(email=email)
            token = _generate_uuid()
            self._db.update_user(user.id, reset_token=token)
            return token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """ method that update the password """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hash_pwd = _hash_password(password)
            self._db.update_user(user.id, hashed_password=hash_pwd,
                                 reset_token=None)
        except NoResultFound:
            raise ValueError
