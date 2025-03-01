# ========= Zadanie 6 =============
class ElectricVehicle:
    def fuel_type(self) -> str:
        return "electric"

class GasolineVehicle:
    def fuel_type(self) -> str:
        return "gasoline"

class HybridCar(ElectricVehicle, GasolineVehicle):
    def fuel_type(self) -> str:
        return "hybrid"

print(ElectricVehicle().fuel_type())
print(GasolineVehicle().fuel_type())
print(HybridCar().fuel_type())