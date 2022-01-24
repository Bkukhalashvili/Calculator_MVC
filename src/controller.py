from src.model import Model
from src.view import View

class Controller:
    
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        self.view.main()
    
    def button_click(self, num):
        self.view.equation.set(self.model.button_click(num))

    def equals(self):    
        self.view.equation.set(self.model.equals())

    def percent(self):
        self.view.equation.set(self.model.percent())

    def plus_or_minus(self):
        self.view.equation.set(self.model.plus_or_minus())

    def delete(self):
        self.view.equation.set(self.model.delete())

    def clear(self):
        self.view.equation.set(self.model.clear())
