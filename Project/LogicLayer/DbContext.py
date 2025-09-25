import datetime
from typing import Self, Optional

from rich import print

from Project.LogicLayer.Books.Book import Book
from Project.LogicLayer.Borrows.Borrow import Borrow
from Project.LogicLayer.Strategies.BorrowStrategy import BorrowStrategy
from Project.LogicLayer.Users.User import UserBuilder, User
from Project.LogicLayer.Decorators import Access_check


class Database:
    # Seed wstępnych danych
    user_builder = UserBuilder()
    Student = (user_builder.set_role().set_first_name("Robert").set_last_name("Student").set_pesel("12341234123")
         .set_password("password").set_birth_date("26-07-1999").build())
    Admin = (user_builder.set_role("Admin").set_first_name("Robert").set_last_name("Admin").set_pesel("12312312312")
         .set_password("password").set_birth_date("26-07-1999").build())

    users: list[User] = [
        Student,
        Admin
    ]
    books: list[Book] = [
        Book("Lalka", "Bolesław Prus", "9781784351151", 1890, "Powieść realistyczna"),
        Book("Zbrodnia i kara", "Fiodor Dostojewski", "9788373273122", 1866, "Powieść psychologiczna"),
        Book("Pan Tadeusz", "Adam Mickiewicz", "9788373272286", 1834, "Epopeja narodowa"),
        Book("Hobbit", "J.R.R. Tolkien", "9780547928227", 1937, "Fantasy"),
        Book("Mały Książę", "Antoine de Saint-Exupéry", "9788390098395", 1943, "Baśń filozoficzna"),
        Book("Władca Pierścieni", "J.R.R. Tolkien", "9788328726291", 1954, "Fantasy")
    ]
    borrows: list[Borrow] = []

    # kontruktor zapewniający, że nie powstanie druga instancja klasy Database
    _instance: Self = None
    def __new__(cls, *args: list, **kwargs: dict) -> Self:
        if cls._instance is None:
            instance = super().__new__(cls, *args, **kwargs)
            cls._instance = instance

        return cls._instance

    # Login po peselu i haśle, jeśli udany to zwraca odpowiedniego użytkonika
    def login(self, pesel: str, password: str) -> User | None:
        for user in self.users:
            if user.pesel == pesel and user.password == password:
                return user
        print("[red]:cross_mark:  Login failed[/red]")
        return None

    # Rejestracja wykorzystująca UserBuildera do utworzenia użytkownika krok po kroku
    def register(self, firstname:str, lastname:str, pesel:str, password:str, birth_date: str) -> None:
        if any(u.pesel == pesel for u in self.users):
            print("[red]User already registered[/red]")
            return

        try:
            user_builder = UserBuilder()
            user = (user_builder.set_role("Student").set_first_name(firstname).set_last_name(lastname).set_pesel(pesel)
                    .set_password(password).set_birth_date(birth_date).build())
            self.users.append(user)
            print("[green]User registered successfully[/green]")
        except ValueError:
            print("[red]Failed to register user[/red]")

    # Pobranie listy książek z bazy
    def get_books(self) -> list[Book]:
        return sorted(self.books, key=lambda book: book.title)

    def get_book_by_isbn(self, isbn: str) -> Book | None:
        book = next((b for b in self.books if b.isbn == isbn), None)

        return book

    @Access_check(["Teacher", "Admin"])
    def add_book(self, book: Book, user=None) -> None:
        if not all([book.author, book.title, book.isbn, book.publication_year, book.genre]):
            print("[red]All fields must not be empty before adding book[/red]")
            return

        if not book.isbn.isdigit():
            print("[red]ISBN must be a number[/red]")
            return

        book_check = self.get_book_by_isbn(book.isbn)

        if book_check:
            print(f"[red] Book with this isbn: ({book_check.isbn}) already registered[/red]")
            return

        self.books.append(book)
        print("[green]Book added[/green]")

    @Access_check(["Teacher", "Admin"])
    def edit_book(self, isbn: str, updated_fields: dict, user=None) -> None:
        book = self.get_book_by_isbn(isbn)
        if book:
            for key, value in updated_fields.items():
                if hasattr(book, key):
                    setattr(book, key, value)
            print(f"[green]Book {isbn} updated successfully.[/green]")
            return
        print(f"[red]Book ({isbn}) not found.[/red]")

    @Access_check(["Teacher", "Admin"])
    def remove_book(self, isbn: str, user=None) -> None:
        book = self.get_book_by_isbn(isbn)

        if not book:
            print(f"[red]Book ({isbn}) not found.[/red]")
            return
        else:
            self.books.remove(book)
            print(f"[yellow]Book ({isbn}) '{book.title}' {book.author} - removed successfully.[/yellow]")

    @Access_check(["Student", "Teacher", "Admin"])
    def borrow_book(self, isbn: str, borrow_strategy: BorrowStrategy, user=None) -> None:
        book = self.get_book_by_isbn(isbn)
        if not book:
            print(f"[red]Book ({isbn}) not found.[/red]")
            return

        borrow_check = any([b.book.isbn == isbn for b in self.borrows])
        if borrow_check:
            print(f"[yellow]Book ({isbn}) - {book.title}, is not available[yellow]")
            return

        borrow = Borrow(user, book, borrow_strategy)
        self.borrows.append(borrow)

        date = datetime.datetime.now()
        date_str = date.strftime("%d.%m.%Y, %H:%M:%S")

        user.operation_hist.append({
            "date": date_str,
            "type": "borrow",
            "isbn": isbn,
        })

        print(f"[green]Book ({isbn}) {book.title} - successfully borrowed[/green]")
        print(f"[blue]Please return book before {borrow.borrowed_until_date}[/blue]")

    @Access_check(["Student", "Teacher", "Admin"])
    def return_book(self, isbn: str, user=None) -> None:
        book = self.get_book_by_isbn(isbn)
        if not book:
            print(f"[red]Book ({isbn}) not found[/red]")
            return

        borrow = next((b for b in self.borrows if b.book.isbn == isbn and b.user.pesel == user.pesel), None)
        if not borrow:
            print(f"[yellow]Cannot return book ({isbn}) as it is not borrowed[/yellow]")
            return

        self.borrows.remove(borrow)

        date = datetime.datetime.now()
        date_str = date.strftime("%d.%m.%Y, %H:%M:%S")

        user.operation_hist.append({
            "date": date_str,
            "type": "return",
            "isbn": isbn,
        })

        print(f"[green]Book ({isbn}) {book.title} - successfully returned[/green]")

        book.notify()

    @Access_check(["Student", "Teacher", "Admin"])
    def show_borrowed(self, user=None) -> Optional[list[Borrow]] :
        user_borrows = [b for b in self.borrows if b.user.pesel == user.pesel]

        if len(user_borrows) == 0:
            print(f"[cyan]No borrowed[/cyan]")
            return None

        return user_borrows

    @Access_check(["Student", "Teacher", "Admin"])
    def reserve_book(self, isbn: str, user=None) -> None:
        book = self.get_book_by_isbn(isbn)
        if not book:
            print(f"[red]Book ({isbn}) not found[/red]")
            return

        borrowed = any(b.book.isbn == isbn for b in self.borrows)
        if not borrowed:
            print(f"[yellow]Book ({isbn}) is available — no need to reserve.[/yellow]")
            return

        user_borrowed = any(b.user == user for b in self.borrows)
        if user_borrowed:
            print(f"[yellow]You already borrow this book[/yellow]")
            return

        if user in book.observers:
            print("[yellow]You have already reserved this book.[/yellow]")
            return

        book.register_reservation(user)
        print(f"[green]Book ({isbn}) {book.title} - successfully reserved[/green]")