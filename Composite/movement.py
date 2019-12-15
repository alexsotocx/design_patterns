class Movement:
    def execute(self):
        raise NotImplementedError("Abstract method")

    def add(self, _step):
        raise Exception("Not supported")

    def name(self):
        raise NotImplementedError("Abstract method")

    def duration(self):
        raise NotImplementedError("Abstract method")

