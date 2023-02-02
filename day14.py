# 10.2
class Thing2:
    letter = 'abc'
    print(letter)


# 10.3
class Thing3:
    print(Thing2.letter)


# 10.4
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):     # 10.6
        print(self.name, self.symbol, self.number)


obj = Element('Hydrogen', 'H', 1)

el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(el_dict['name'], el_dict['symbol'], el_dict['number'])   # 10.5

hydrogen.dump()    # 10.6




