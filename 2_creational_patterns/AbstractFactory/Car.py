from abc import ABC, abstractmethod
from typing import Any

# Utworzyć Fabrykę Abstrakcyjną do produkcji samochodów różnych marek (TeslaFactory, BMWFactory).
# Każda z fabryk powinna produkować dwa typy samochodów według nadwozia: Sedan i SUV.

class Car(ABC):
    @abstractmethod
    def getInfo(self) -> None:
        pass

class SedanCar(Car):
    def getInfo(self) -> str:
        return "Sedan car"

class SUVCar(Car):
    def getInfo(self) -> str:
        return "SUV car"

class CarFactory(ABC):
    @abstractmethod
    def createSedan(self) -> None:
        pass

    @abstractmethod
    def createSUV(self) -> None:
        pass

class TeslaFactory(CarFactory):
    def createSedan(self) -> SedanCar:
        return TeslaSedan()

    def createSUV(self) -> SUVCar:
        return TeslaSUV()

class TeslaSedan(SedanCar):
    pass

class TeslaSUV(SUVCar):
    pass

class BMWFactory(CarFactory):
    def createSedan(self) -> SedanCar:
        return BMWSedan()

    def createSUV(self) -> SUVCar:
        return BMWSUV()

class BMWSedan(SedanCar):
    pass

class BMWSUV(SUVCar):
    pass

class AbstractCarFactory:
    @staticmethod
    def get_factory(brand: str) -> Any:
        match brand:
            case "Tesla":
                return TeslaFactory()
            case "BMW":
                return BMWFactory()
            case _:
                raise ValueError


teslaFactory = AbstractCarFactory.get_factory("Tesla")
teslaSedan = teslaFactory.createSedan()
teslaSUV = teslaFactory.createSUV()
print(teslaSedan.getInfo())
print(teslaSUV.getInfo())