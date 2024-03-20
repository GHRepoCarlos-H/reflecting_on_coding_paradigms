

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
            self.condition = "repaired"


class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2


class SebulbasPod(Podracer):
    def flame_jet(self, other_podracer):
        other_podracer.condition = "trashed"

if __name__ == "__main__":

    podracer1 = Podracer(max_speed=200, condition="Perfect", price=1000)
    anakins_pod = AnakinsPod(max_speed=300, condition="Perfect", price=1300)
    sebulbas_pod = SebulbasPod(max_speed=250, condition="Perfect", price=1200)

    podracer1.repair()
    anakins_pod.boost()
    sebulbas_pod.flame_jet(podracer1)

    print("podracer 1 condition is:", podracer1.condition)
    print("Anakin's max speed:", anakins_pod.max_speed)
    print("Sebulba's pod condition (Podracer 1):",podracer1.condition)