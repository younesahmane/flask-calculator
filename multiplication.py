from flask import Flask
from calculator import Calculator


class Addition(Calculator):
    def calculate(self):
        return self.numberA * self.numberB