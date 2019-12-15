from movement import Movement


class DanceStep(Movement):
    def __init__(self, step_name, step_duration):
        self.__name = step_name
        self.__duration = step_duration

    def execute(self):
        print("Executing {name}".format(name=self.name()))

    def name(self):
        return self.__name

    def duration(self):
        return self.__duration

