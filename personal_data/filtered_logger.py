#!/usr/bin/env python3
""" returns the log message obfuscated
"""
import re
import typing
import logging
import os
import mysql.connector


def filter_datum(fields: typing.List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
    fields: a list of strings representing all fields to obfuscate
    redaction: a string representing by what the field will be obfuscated
    message: a string representing the log line
    separator: a string representing by which character is separating
    all fields in the log line (message)
    """
    for field in fields:
        message = re.sub(rf"{field}=(.+?){separator}",
                         f"{field}={redaction}{separator}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: typing.List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ update function format of parent class
            for add a filter
        """
        msg = super().format(record)
        return filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)


PII_FIELDS = ("name", "email", "phone", "password", "ssn")


def get_logger() -> logging.Logger:
    """ get logger """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    logger.addHandler(console_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ create db conncetion """
    username_db = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password_db = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host_db = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
        host=host_db,
        user=username_db,
        password=password_db,
        database=db_name
    )
