# ========= Zadanie 20 =============
from abc import ABC, abstractmethod


class Instrument(ABC):
    @abstractmethod
    def play(self) -> None:
        pass

class Piano(Instrument):
    def play(self) -> str:
        return "Piano play"

class Guitar(Instrument):
    def play(self) -> str:
        return "Guitar play"

print(Piano().play())
print(Guitar().play())