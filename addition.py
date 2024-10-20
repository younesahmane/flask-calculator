from flask import Flask
from abstract_class_calculation import Calculator


class Addition(Calculator):
    def calculate(self, num1, num2):
        return num1 + num2