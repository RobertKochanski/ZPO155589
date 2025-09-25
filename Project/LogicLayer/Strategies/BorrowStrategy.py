import datetime
from abc import ABC, abstractmethod


class BorrowStrategy(ABC):
    @abstractmethod
    def borrow_book(self, current_date: datetime.date = datetime.date.today()) -> datetime.date:
        pass

class ShortTermBorrowStrategy(BorrowStrategy):
    def borrow_book(self, current_date: datetime.date = datetime.date.today()) -> datetime.date:
        return current_date + datetime.timedelta(days=7)

class NormalTermBorrowStrategy(BorrowStrategy):
    def borrow_book(self, current_date: datetime.date = datetime.date.today()) -> datetime.date:
        return current_date + datetime.timedelta(days=14)

class LongTermBorrowStrategy(BorrowStrategy):
    def borrow_book(self, current_date: datetime.date = datetime.date.today()) -> datetime.date:
        return current_date + datetime.timedelta(days=30)