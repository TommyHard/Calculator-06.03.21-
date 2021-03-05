import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from math import sqrt

class CalcGridLayout(GridLayout):

    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "не делай так"

    def square_digits(self, calculation):
        if calculation:
            try:
                self.display.text = str(int(calculation) ** 2)
            except Exception:
                self.display.text = "не делай так"

    def divisionByX(self, calculation):
        if calculation:
            try:
                self.display.text = str(1 / int(calculation))
            except Exception:
                self.display.text = "не делай так"

    def square(self, calculation):
        if calculation:
            try:
                self.display.text = str(sqrt(int(calculation)))
            except Exception:
                self.display.text = "не делай так"

class CalculatorApp(App):
    def build(self):
        return CalcGridLayout()
calcApp = CalculatorApp()
calcApp.run()