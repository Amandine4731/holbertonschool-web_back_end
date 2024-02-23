#!/usr/bin/env python3
""" Manager API Authentication """
from flask import request
from typing import List, TypeVar, Tuple
from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user import User
import json


class BasicAuth(Auth):
    """ class BasicAuth inerith from Auth """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ returns the Base64 part of the Authorization header """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if authorization_header.startswith("Basic ") is False:
            return None
        else:
            return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """Returns the decoded value of a Base64 string."""
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            return b64decode(base64_authorization_header).decode('UTF-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """  returns the useremail and pswd from the Base64 decoded value. """
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        else:
            split_str = decoded_base64_authorization_header.split(":")
            user_email = split_str[0]
            password = split_str[1]
            return user_email, password

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str
                                     ) -> TypeVar('User'):
        """  that returns the User instance based on his email and password """
        if type(user_email) is not str or user_email is None:
            return None
        if type(user_pwd) is not str or user_pwd is None:
            return None

        try:
            users = User.search({"email": user_email})
        except Exception:
            return None

        if not users:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user """
        if request is None:
            return None

        header_autorization = self.authorization_header(request)

        if header_autorization:
            base64_auth = self.extract_base64_authorization_header(
                header_autorization)
        else:
            return None

        if base64_auth is not None:
            decode_base64 = self.decode_base64_authorization_header(
                base64_auth)
        else:
            return None

        if decode_base64 is not None:
            extract_credentiel = self.extract_user_credentials(decode_base64)
        else:
            return None

        if extract_credentiel is not None:
            return self.user_object_from_credentials(extract_credentiel[0],
                                                     extract_credentiel[1])
