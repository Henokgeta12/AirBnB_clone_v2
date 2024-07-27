#!usr/bin/python3
"""
A Python script that starts a Flask web application.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slash=False)
def HBNB():
    """
    A route decorator that handles GET requests to the root URL ("/").
    Returns a string "Hello HBNB!".
    """
    return "Hello HBNB!"

if '__name__' == '__main__':
    app.run(host='0.0.0.0', port=5000)
