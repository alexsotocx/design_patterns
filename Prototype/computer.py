import copy


class Computer:
    def __init__(self):
        self.cpu = None
        self.motherboard = None
        self.ram = None

    def clone(self):
        return copy.deepcopy(self)

    def calculate(self, op1, operation, op2):
        return self.cpu.execute(op1, operation, op2)

    def specs(self):
        return """Computer specs:
CPU: {cpu_frequency},
Motherboard: {mb_name},
Memory: {capacity},
""".format(cpu_frequency=self.cpu.frequency,
           mb_name=self.motherboard.model,
           capacity=self.ram.capacity)
