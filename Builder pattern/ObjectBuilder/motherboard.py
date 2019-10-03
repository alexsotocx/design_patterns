class MotherBoard:
    def __init__(self, model):
        self.model = model
        self.powered_on = False

    def toggle_power(self):
        self.powered_on = not self.powered_on
