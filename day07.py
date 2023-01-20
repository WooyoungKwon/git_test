# 10.5
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        # print(class)
        return self.name, self.symbol, self.number


no1 = Element('Hydrogen', 'H', 1)
print(vars(no1))