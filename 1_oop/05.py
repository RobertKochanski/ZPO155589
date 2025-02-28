# ========= Zadanie 5 =============
from dataclasses import dataclass
from datetime import datetime


@dataclass()
class Car:
    brand:str
    model:str
    year:int

    def is_classic(self):
        return datetime.now().year - self.year > 25

car = Car("Fiat", "Punto", 1999)
print(car.is_classic())

car2 = Car("samochod", "Czerwony", 2020)
print(car2.is_classic())