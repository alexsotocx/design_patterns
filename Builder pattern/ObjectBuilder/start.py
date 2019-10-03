from desktop_computer_assembler import DesktopComputerAssembler
from cpu import InstructionSetBuilder

computer = DesktopComputerAssembler() \
    .mount_motherboard('AMD 570') \
    .plug_CPU(
    3800,
    InstructionSetBuilder()
    .add_operation('+', lambda a, b: a + b)
    .add_operation('-', lambda a, b: a - b)
    .build()
) \
    .memory_ram(8192).build()

assert(computer.calculate(5, '-', 2) == 3)
assert(computer.calculate(3, '+', 2) == 5)
print(computer.specs())
try:
    computer.calculate(3, '*', 2)
except:
    print("works")

try:
    computer_without_ram = DesktopComputerAssembler() \
        .mount_motherboard('AMD 570') \
        .plug_CPU(
        3800,
        {},
    ).build()
except:
    print("Exception thrown Invalid computer")
