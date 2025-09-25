from abc import ABC, abstractmethod

from Project.LogicLayer.Interfaces.Observer import Observer


class Observable(ABC):
    @abstractmethod
    def register_reservation(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def remove_reservation(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass