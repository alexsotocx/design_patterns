from movement import Movement
from dance_step import DanceStep
from choreography import Choreography

def do_movement(movement: Movement):
    movement.execute()
    print(movement.duration())
    

double_step = DanceStep("Double Step", 1)
third_step = DanceStep("Third Step", 2)

habana_choreography = Choreography("Habana")
habana_choreography.add(double_step)
habana_choreography.add(double_step)
habana_choreography.add(double_step)
habana_choreography.add(third_step)
habana_choreography.add(third_step)
habana_choreography.add(double_step)

do_movement(double_step)
do_movement(third_step)
do_movement(habana_choreography)
