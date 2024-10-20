from flask import Flask, jsonify
from calculator import Add, Subtract, Multiply, Divide  # Assume this is how classes named

app = Flask(__name__)

@app.route('/add/<int:numberA>/<int:numberB>')
def add_route(numberA, numberB):
    operation = Add(numberA, numberB)
    result = operation.calculate()
    return jsonify({"status": 200, "result": result})

@app.route('/subtract/<int:numberA>/<int:numberB>')
def subtract_route(numberA, numberB):
    operation = Subtract(numberA, numberB)
    result = operation.calculate()
    return jsonify({"status": 200, "result": result})

@app.route('/multiply/<int:numberA>/<int:numberB>')
def multiply_route(numberA, numberB):
    operation = Multiply(numberA, numberB)
    result = operation.calculate()
    return jsonify({"status": 200, "result": result})

@app.route('/divide/<int:numberA>/<int:numberB>')
def divide_route(numberA, numberB):
    try:
        operation = Divide(numberA, numberB)
        result = operation.calculate()
        return jsonify({"status": 200, "result": result})
    except ValueError as e:
        return jsonify({"status": 200, "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
