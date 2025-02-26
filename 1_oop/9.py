# ========= Zadanie 9 =============
class FlyingVehicle:
    def move(self):
        return "I fly"

class WaterVehicle:
    def move(self):
        return "I sail"

class AmphibiousVehicle:
    mode:bool # 0-flying, 1-water

    def __init__(self, mode:bool):
        self.mode = mode

    def move(self):
        if self.mode == False:
            return "I fly"
        elif self.mode:
            return "I sail"
        else:
            return "Something went wrong"

print(FlyingVehicle().move())
print(WaterVehicle().move())
print(AmphibiousVehicle(True).move())
print(AmphibiousVehicle(False).move())