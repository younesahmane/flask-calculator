from abc import ABC, abstractmethod

class Calculator(ABC):
    def __init__(self, numberA: float, numberB: float):
        self.numberA = numberA
        self.numberB = numberB
    
    @abstractmethod
    def calculate(self) -> float:
        pass

class Multiply(Calculator):
    def calculate(self) -> float:
        return self.numberA * self.numberB

class Divide(Calculator):
    def calculate(self) -> float:
        if self.numberB == 0:
            raise ValueError("Division by zero is not allowed")
        return self.numberA / self.numberB
