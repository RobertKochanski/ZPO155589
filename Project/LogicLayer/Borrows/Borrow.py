import datetime

from Project.LogicLayer.Books import Book
from Project.LogicLayer.Strategies import BorrowStrategy
from Project.LogicLayer.Users import User


class Borrow:
    user: User
    book: Book
    borrow_date: datetime.date
    borrowed_until_date: BorrowStrategy

    def __init__(self, user: User, book: Book, strategy: BorrowStrategy):
        self.user = user
        self.book = book
        self.borrow_date = datetime.date.today()
        self.borrowed_until_date = strategy.borrow_book(self.borrow_date)

    def __str__(self):
        return (f"{self.book.title} borrowed by {self.user.firstname} {self.user.lastname} "
                f"on {self.borrow_date}, until {self.borrowed_until_date}")
