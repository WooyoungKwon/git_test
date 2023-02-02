# 10.4
class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    # 10.8
    @property
    def get_name(self):
        return self.__name

    @property
    def get_symbol(self):
        return self.__symbol

    @property
    def get_number(self):
        return self.__number

    # 10.7
    def __str__(self):
        return self.__name


el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(el_dict['name'], el_dict['symbol'], el_dict['number'])   # 10.5
print(hydrogen.get_number, hydrogen.get_symbol, hydrogen.get_name)





