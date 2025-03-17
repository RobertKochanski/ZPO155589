from abc import ABC, abstractmethod
from typing import Any


class Car(ABC):
    @abstractmethod
    def checkCarType(self) -> None:
        pass

class SedanCar(Car):
    def checkCarType(self) -> str:
        return "Sedan car"

class SUVCar(Car):
    def checkCarType(self) -> str:
        return "SUV car"

class HatchbackCar(Car):
    def checkCarType(self) -> str:
        return "Hatchback car"

class CarFactory(ABC):
    @abstractmethod
    def createSedan(self) -> None:
        pass

    @abstractmethod
    def createSUV(self) -> None:
        pass

    @abstractmethod
    def createHatchback(self) -> None:
        pass

class TeslaSedan(SedanCar):
    def checkCar(self) -> str:
        return "Tesla Sedan - check"

class TeslaSUV(SUVCar):
    def checkCar(self) -> str:
        return "Tesla SUV - check"

class TeslaHatchback(HatchbackCar):
    def checkCar(self) -> str:
        return "Tesla Hatchback - check"

class TeslaFactory(CarFactory):
    def createSedan(self) -> SedanCar:
        return TeslaSedan()

    def createSUV(self) -> SUVCar:
        return TeslaSUV()

    def createHatchback(self) -> HatchbackCar:
        return TeslaHatchback()


class BMWSedan(SedanCar):
    def checkCar(self) -> str:
        return "BMW Sedan - check"

class BMWSUV(SUVCar):
    def checkCar(self) -> str:
        return "BMW SUV - check"

class BMWHatchback(HatchbackCar):
    def checkCar(self) -> str:
        return "BMW Hatchback - check"

class BMWFactory(CarFactory):
    def createSedan(self) -> SedanCar:
        return BMWSedan()

    def createSUV(self) -> SUVCar:
        return BMWSUV()

    def createHatchback(self) -> HatchbackCar:
        return BMWHatchback()

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


# Testing Tesla
teslaFactory = AbstractCarFactory.get_factory("Tesla")
teslaSedan = teslaFactory.createSedan()
teslaSUV = teslaFactory.createSUV()
teslaHatchback = teslaFactory.createHatchback()
print(teslaSedan.checkCarType())
print(teslaSedan.checkCar())
print(teslaSUV.checkCarType())
print(teslaSUV.checkCar())
print(teslaHatchback.checkCarType())
print(teslaHatchback.checkCar())

# Testing BMW
BmwFactory = AbstractCarFactory.get_factory("BMW")
bmwSedan = BmwFactory.createSedan()
print(bmwSedan.checkCarType())
print(bmwSedan.checkCar())