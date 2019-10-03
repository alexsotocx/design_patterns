class CPU:
    def __init__(self, frequency, instruction_set):
        self.frequency = frequency
        self.instruction_set = instruction_set

    def execute(self, operand1, operation, operand2):
        if operation in self.instruction_set:
            function = self.instruction_set[operation]
            return function(operand1, operand2)
        else:
            raise NotImplementedError()


class InstructionSetBuilder:
    __instructions = {}

    def add_operation(self, identifier, operation):
        self.__instructions[identifier] = operation
        return self

    def build(self):
        return self.__instructions
