#!/usr/bin/env python3
""" Manager API Authentication """
import os
from flask import request
from typing import List, TypeVar


class Auth():
    """ class manage the API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Check if authentication is required for a given path. """

        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        if path in excluded_paths or path + "/" in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ Get the authorization header from the Flask request object. """
        if request is None:
            return None
        if "Authorization" not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get the current user from the Flask request object. """
        return None

    def session_cookie(self, request=None):
        """  returns a cookie value from a request """
        if request is None:
            return None
        cookie_name = os.environ.get("SESSION_NAME")
        cookie_value = request.cookies.get(cookie_name)
        return cookie_value
