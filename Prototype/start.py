from computer import Computer
from cpu import CPU
from memory import RAM
from motherboard import MotherBoard
from prototype_registry import PrototypeRegistry

registry = PrototypeRegistry()
# CPU
ryzen5 = CPU("AMD Ryzen 5 3600", None)
ryzen7 = CPU("AMD Ryzen 7 3700X", None)
ryzen9 = CPU("AMD Ryzen 9 3900", None)

# RAM
gskill3200mhz = RAM(3200)
gskill3000mhz = RAM(3000)
gskill3600mhz = RAM(3600)

# Motherboard
AMDB450 = MotherBoard("AMDB450")
AMDX570 = MotherBoard("AMDX570")
AMDB470 = MotherBoard("AMDB470")


registry.register("ryzen5", ryzen5)
registry.register("ryzen7", ryzen7)
registry.register("ryzen9", ryzen9)
registry.register("gskill3200mhz", gskill3200mhz)
registry.register("gskill3000mhz", gskill3000mhz)
registry.register("gskill3600mhz", gskill3600mhz)
registry.register("AMDB450", AMDB450)
registry.register("AMDX570", AMDX570)
registry.register("AMDB470", AMDB470)


def build_computer(cpu, ram, motherboard):
    computer = Computer()
    computer.motherboard = motherboard
    computer.cpu = cpu
    computer.ram = ram

    return computer


pro_computer = build_computer(
    registry.clone("ryzen9"), registry.clone("gskill3600mhz"), registry.clone("AMDX570"))

bugdget_computer = build_computer(
    registry.clone("ryzen5"), registry.clone("gskill3000mhz"), registry.clone("AMDB450"))

print(pro_computer.specs())
print(bugdget_computer.specs())

registry.register("pro_computer", pro_computer)

pro2_computer = registry.clone("pro_computer")

if pro2_computer.ram == pro_computer.ram:
    print("They should not be equal")
else:
    print("They have the same specs but different parts")
