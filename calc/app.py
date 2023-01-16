# Put your app in here.

# First we must import Flask
# and by importing a flask object called request 
from flask import Flask, request

# Import math operations file
import operations
# from operations import add, sub, mult, div

# This command initiates server - tells flask to do it's thing in the file.
app = Flask(__name__)

@app.route('/add')
def add_route():

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    result = operations.add(a,b)

    return str(result)

@app.route('/sub')
def sub_route():

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    result = operations.sub(a,b)

    return str(result)

@app.route('/mult')
def mult_route():

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    result = operations.mult(a,b)

    return str(result)

@app.route('/div')
def div_route():

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    result = operations.div(a,b)

    return str(result)

operators = {
    "add": operations.add,
    "sub": operations.sub,
    "mult": operations.mult,
    "div": operations.div,
}

@app.route('/math/<op>')
def math_route(op):

    op_to_perform = operators[op]

    print(op_to_perform)

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    result = op_to_perform(a,b)

    return str(result)