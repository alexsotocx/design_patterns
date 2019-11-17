class PrototypeRegistry:
    def __init__(self):
        self._prototypes = {}

    def clone(self, key):
        return self._prototypes[key].clone()

    def register(self, key, object_clone):
        self._prototypes[key] = object_clone
