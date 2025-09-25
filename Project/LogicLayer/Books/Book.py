from Project.LogicLayer.Interfaces.Component import Component
from Project.LogicLayer.Interfaces.Observable import Observable
from Project.LogicLayer.Interfaces.Observer import Observer

class Book(Component, Observable):
    title: str
    author: str
    isbn: str
    publication_year: int
    genre: str

    def __init__(self, title: str, author: str, isbn: str, publication_year: int, genre: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.genre = genre

        self.observers: list[Observer] = []

    def to_table(self) -> list[list[str]]:
        return [[None, self.isbn, self.title, self.genre, str(self.publication_year)]]

    # Implementacja Observable dla książki
    def register_reservation(self, observer: Observer) -> None:
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_reservation(self, observer: Observer) -> None:
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self) -> None:
        if self.observers:
            next_user = self.observers.pop(0)
            next_user.notify(self)