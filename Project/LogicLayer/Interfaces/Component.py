from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def to_table(self) -> None:
        pass