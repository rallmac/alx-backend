#!/usr/bin/env python3
"""This is a flask app that prints hello world
   and the heading is welcome to holberton
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)


class Config:
    """Configuration for Flask app and Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Set up the app config
app.config.from_object(Config)

# Instantiate the Babel object
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Select the best match for supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """This is the route of the app"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
