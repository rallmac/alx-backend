#!/usr/bin/env python3
"""This is a flask application that displays
   welcome to holberton
"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """This is the route of the app"""
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True, port=5000)
