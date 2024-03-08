#!/usr/bin/env python3
"""
flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


class Config():
    """ class Config """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def index():
    """ index """
    return render_template("3-index.html")


@babel.localeselector
def get_locale() -> str:
    """ get local languages """
    return request.accept_languages.best_match(Config.LANGUAGES)
