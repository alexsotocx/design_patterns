from builder import Builder


class BitBuilder(Builder):
    def __init__(self):
        self.__result = []

    def result(self):
        return self.__result

    def __transform(self, char):
        if char == ' ':
            pass
        else:
            binary = bin(ord(char))
            self.__result.append(binary[2:])

    def transform_number(self, number):
        self.__transform(number)

    def transform_symbol(self, symbol):
        self.__transform(symbol)

    def transform_letter(self, letter):
        self.__transform(letter)
