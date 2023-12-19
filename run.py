import os
import sys
import pip._vendor.requests 

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
  response = pip._vendor.requests.get('https://function-76.1at6rgz00yjr.eu-de.codeengine.appdomain.cloud')
  