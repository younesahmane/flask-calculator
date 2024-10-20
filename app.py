from flask import Flask, jsonify
from calculator import Multiply, Divide  # Assume this is how classes named
from addition import Addition
from substraction import Substraction
app = Flask(__name__)

def convertNumber(number): #Handling both int and float, straight forward
    try:
        return int(number)
    except ValueError:
        return float(number)


@app.route('/add/<path:numberA>/<path:numberB>')
def add_route(numberA, numberB):
    numberA = convertNumber(numberA)
    numberB = convertNumber(numberB)
    operation = Addition(numberA, numberB)
    result = operation.calculate()
    return jsonify({"status": 200, "result": result})

@app.route('/subtract/<path:numberA>/<path:numberB>')
def subtract_route(numberA, numberB):
    numberA = convertNumber(numberA)
    numberB = convertNumber(numberB)
    operation = Substraction(numberA, numberB)
    result = operation.calculate()
    return jsonify({"status": 200, "result": result})

@app.route('/multiply/<path:numberA>/<path:numberB>')
def multiply_route(numberA, numberB):
    numberA = convertNumber(numberA)
    numberB = convertNumber(numberB)
    operation = Multiply(numberA, numberB)
    result = operation.calculate()
    return jsonify({"status": 200, "result": result})

@app.route('/divide/<path:numberA>/<path:numberB>')
def divide_route(numberA, numberB):
    numberA = convertNumber(numberA)
    numberB = convertNumber(numberB)
    try:
        operation = Divide(numberA, numberB)
        result = operation.calculate()
        return jsonify({"status": 200, "result": result})
    except ValueError as e:
        return jsonify({"status": 200, "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
