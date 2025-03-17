from abc import ABC, abstractmethod
from typing import Any


class Smartfon(ABC):
    @abstractmethod
    def smartfonType(self) -> None:
        pass

class Apfel(Smartfon):
    model:str

    def __init__(self, model):
        self.model = model

    def smartfonType(self) -> str:
        return f"Smartfon type: Apfel \nmodel: {self.model}"

class Szajsung(Smartfon):
    model: str

    def __init__(self, model):
        self.model = model

    def smartfonType(self) -> str:
        return f"Smartfon type: Szajsung \nmodel: {self.model}"

class MajFon(Smartfon):
    model: str

    def __init__(self, model):
        self.model = model

    def smartfonType(self) -> str:
        return f"Smartfon type: MajFon \nmodel: {self.model}"

class SmartfonFactory(ABC):
    @abstractmethod
    def createSmartfon(self, model:str) -> None:
        pass

class ApfelFactory(SmartfonFactory):
    def createSmartfon(self, model:str) -> Apfel:
        return Apfel(model)

class SzajsungFactory(SmartfonFactory):
    def createSmartfon(self, model:str) -> Szajsung:
        return Szajsung(model)

class MajFonFactory(SmartfonFactory):
    def createSmartfon(self, model:str) -> MajFon:
        return MajFon(model)

class AbstractFactory:
    @staticmethod
    def getFactory(type: str) -> Any:
        match type:
            case "Apfel":
                return ApfelFactory()
            case "Szajsung":
                return SzajsungFactory()
            case "MajFon":
                return MajFonFactory()
            case _:
                raise ValueError


apfelFactory = AbstractFactory().getFactory("Apfel")
apfelFrom2024 = apfelFactory.createSmartfon("model from 2024")
print(apfelFrom2024.smartfonType())

szajsungFactory = AbstractFactory().getFactory("Szajsung")
szajsungFrom2022 = szajsungFactory.createSmartfon("model from 2022")
print(szajsungFrom2022.smartfonType())

majFonFactory = AbstractFactory().getFactory("MajFon")
majFonFrom2025 = majFonFactory.createSmartfon("model from 2025")
print(majFonFrom2025.smartfonType())