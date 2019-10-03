from cpu import CPU
from motherboard import MotherBoard
from memory import RAM


class Computer:
    cpu = None
    motherboard = None
    ram = None

    def calculate(self, op1, operation, op2):
        return self.cpu.execute(op1, operation, op2)


class DesktopComputerAssembler:
    __computer = None

    def __init__(self):
        self.__computer = Computer()

    def plug_CPU(self, frequency, instruction_set):
        self.__computer.cpu = CPU(frequency, instruction_set)
        return self

    def mount_motherboard(self, motherboard_model):
        self.__computer.motherboard = MotherBoard(motherboard_model)
        return self

    def memory_ram(self, capacity):
        self.__computer.ram = RAM(capacity)
        return self

    def build(self):
        if self.__computer.ram is None:
            raise RuntimeError("Computer without Ram")

        # ...
        return self.__computer
