# ========= Zadanie 18 =============
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def max_speed(self) -> None:
        pass

class Car(Vehicle):
    def max_speed(self) -> float:
        return 400

class Bicycle(Vehicle):
    def max_speed(self) -> float:
        return 40

print(Car().max_speed())
print(Bicycle().max_speed())