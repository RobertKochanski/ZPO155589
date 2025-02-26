# ========= Zadanie 3 =============
from dataclasses import dataclass


@dataclass()
class Book:
    title: str
    author: str
    year: int
    price: float

    def apply_discount(self, discount: int):
        self.price -=  round(self.price * discount / 100, 2)

book = Book("title", "author", 1999, 9.99)
print(f"Before: {book})")
book.apply_discount(50)
print(f"After: {book})")
