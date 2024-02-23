#!/usr/bin/env python3
""" encrypt password"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ hash password """
    return bcrypt.hashpw(password.encode("UTF-8"), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ check is password and hashed_password are the same """
    return bcrypt.checkpw(password.encode("UTF-8"), hashed_password)
