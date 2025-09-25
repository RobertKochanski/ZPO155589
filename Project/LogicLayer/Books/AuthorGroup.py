from Project.LogicLayer.Books import Book
from Project.LogicLayer.Interfaces.Component import Component


class AuthorGroup(Component):
    author: str
    book: list[Book]

    def __init__(self, author: str):
        self.author = author
        self.books: list[Book] = []

    def add(self, book: Book) -> None:
        self.books.append(book)

    def to_table(self) -> list[list[str]]:
        rows = [[self.author, "", "", "", ""]]
        for book in sorted(self.books, key=lambda x: x.title):
            rows += book.to_table()
        return rows