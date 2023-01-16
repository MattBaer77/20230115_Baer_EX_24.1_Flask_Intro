# First we must import Flask
# and by importing a flask object called request 
from flask import Flask, request

# This command initiates server - tells flask to do it's thing in the file.
app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return "Welcome"

@app.route('/welcome/home')
def welcome_home():
    return "Welcome Home"

@app.route('/welcome/back')
def welcome_back():
    return "Welcome Back"