class Appliance:
    def turn_on(self):
        print("Appliance is on")


class WashingMachine(Appliance):
    def __init__(self, washing_mode):
        self.washing_mode = washing_mode

    def turn_on(self):
        print("Washing machine on in", self.washing_mode, "mode")


WashingMachine("Quick").turn_on()
