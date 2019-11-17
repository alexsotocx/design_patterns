import copy


class RAM:
    def __init__(self, capacity):
        self.capacity = capacity

    def clone(self):
        return copy.copy(self)
