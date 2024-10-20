from calculator import Add, Subtract, Multiply, Divide
class CalculatorController:
    def add(self, numberA: float, numberB: float) -> float:
        operation = Add(numberA, numberB)
        return operation.calculate()

    def subtract(self, numberA: float, numberB: float) -> float:
        operation = Subtract(numberA, numberB)
        return operation.calculate()

    def multiply(self, numberA: float, numberB: float) -> float:
        operation = Multiply(numberA, numberB)
        return operation.calculate()

    def divide(self, numberA: float, numberB: float) -> float:
        operation = Divide(numberA, numberB)
        return operation.calculate()