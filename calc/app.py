# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

#Hard Coded version:

# @app.route('/add')
# def add():
#     a = int(request.args["a"])
#     b = int(request.args["b"])
#     return f"{a+b}"

@app.route('/add')
def add_nums():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = add(a,b)
    return str(result)

@app.route('/subtract')
def sub_nums():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = sub(a,b)
    return str(result)

@app.route('/mult')
def mult_nums():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = mult(a,b)
    return str(result)

@app.route('/div')
def div_nums():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = div(a,b)
    return str(result)
    















