# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 12:45:37 2020

@author: Admin
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()