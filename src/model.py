class Model:
    def __init__(self):
        self.expression = ''

    def button_click(self, num):
        self.expression = self.expression + str(num)
        return self.expression
        
    def equals(self):
        try:
            total = str(eval(self.expression))
            self.expression = total
            return self.expression
        except:
            self.expression = ''
            return 'ERROR'

    def percent(self):
        if '.' in self.expression:
            self.expression =  float(self.expression) / 100
            self.expression =  str(self.expression)
            return self.expression
        else:
            self.expression =  int(self.expression)/100
            self.expression =  str(self.expression)
            return self.expression
    
    def plus_or_minus(self):
        if self.expression.startswith('-'):
            self.expression = self.expression[1:]
            return self.expression
        else:
            self.expression = '-' + self.expression
            return self.expression

    def delete(self):
        self.expression = self.expression[:-1]
        return self.expression

    def clear(self):
        self.expression = ''
        return self.expression      
