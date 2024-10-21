from flask import Flask
from calculator import Calculator


class Substraction(Calculator):
    def calculate(self):
        return self.numberA / self.numberB