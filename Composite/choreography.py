from movement import Movement


class Choreography(Movement):
    def __init__(self, c_name):
        self.__name = c_name
        self.__steps = []

    def execute(self):
        print("Executing Choreography: {name} with duration {duration}".format(
            name=self.name(), duration=self.duration()))
        for step in self.__steps:
            step.execute()
        print("Finished")

    def add(self, step):
        self.__steps.append(step)

    def duration(self):
        __duration = 0
        for step in self.__steps:
            __duration += step.duration()

        return __duration

    def name(self):
        return self.__name

