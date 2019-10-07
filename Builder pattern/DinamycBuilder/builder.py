class Builder:
    def result(self):
        raise NotImplementedError

    def transform_number(self, number):
        pass

    def transform_symbol(self, symbol):
        pass

    def transform_letter(self, letter):
        pass
