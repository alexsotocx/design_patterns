class MotherBoard:
    model = "standard model"
    powered_on = True

    def __init__(self, model):
        self.model = model

    def toggle_power(self):
        self.powered_on = not self.powered_on
