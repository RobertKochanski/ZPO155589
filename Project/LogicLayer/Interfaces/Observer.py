from abc import ABC, abstractmethod

from Project.LogicLayer.Books import Book


class Observer(ABC):
    @abstractmethod
    def notify(self, book: Book) -> None:
        pass