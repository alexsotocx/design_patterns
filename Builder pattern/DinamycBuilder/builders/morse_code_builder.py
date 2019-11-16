from builder import Builder


class MorseCodeBuilder(Builder):
    __letter_dic = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
    }

    __symbol_dic = {
        "&": '.-...',
        "'": '.----.',
        "@": '.--.-.',
        ")": '-.--.-',
        "(": '-.--.',
        ":": '---...',
        ",": '--..--',
        "=": '-...-',
        "!": '-.-.--',
        ".": '.-.-.-',
        "-": '-....-',
        "+": '.-.-.',
        "\"": '.-..-.',
        "?": '..--..',
        "/": '-..-.',
        " ": '',
    }

    __number_dic = {
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
    }

    def __init__(self):
        super().__init__()
        self.__result = []

    def result(self):
        return ''.join(self.__result)

    def transform_number(self, number):
        self.__result.append(self.__number_dic[number])

    def transform_symbol(self, symbol):
        self.__add_char(symbol, self.__symbol_dic)

    def transform_letter(self, letter):
        self.__add_char(MorseCodeBuilder.upper_case(letter), self.__letter_dic)

    @staticmethod
    def upper_case(letter):
        num = ord(letter)
        num = (((1 << 10) - 1) - (1 << 5)) & num
        return chr(num)

    def __add_char(self, char, dic):
        if char in dic:
            self.__result.append(dic[char])
        else:
            print("Error adding symbol")
            print(char)
            raise RuntimeError
