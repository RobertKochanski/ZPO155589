# ========= Zadanie 6 =============
class ElectricVehicle:
    def fuel_type(self):
        return "electric"

class GasolineVehicle:
    def fuel_type(self):
        return "gasoline"

class HybridCar(ElectricVehicle, GasolineVehicle):
    def fuel_type(self):
        return "hybrid"

print(ElectricVehicle().fuel_type())
print(GasolineVehicle().fuel_type())
print(HybridCar().fuel_type())