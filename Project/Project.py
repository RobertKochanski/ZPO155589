from typing import Self
from abc import ABC, abstractmethod
import datetime
import typer


# Dekorator sprawdzający czy użytkonik ma potrzebną rolę
def Access_check(roles: list[str]):
    def decorator(fn: callable) -> callable:
        def wrapper(*args, **kwargs):
            user = kwargs.get("user")
            if not user:
                raise ValueError("User not found!")
            if user.role not in roles:
                raise PermissionError(f"Access denied. Needed role: {roles}")
            return fn(*args, **kwargs)
        return wrapper
    return decorator


# Klasa użytkownika i builder wykorzystany do jego tworzenia
class User:
    role: str
    firstname: str
    lastname: str
    pesel: str
    password: str
    birth_date: datetime.datetime

    def __init__(self, role: str, firstname: str, lastname: str, pesel: str, password: str, birth_date: datetime.datetime):
        self.role = role
        self.firstname = firstname
        self.lastname = lastname
        self.pesel = pesel
        self.password = password
        self.birth_date = birth_date

    def __str__(self):
        date = datetime.datetime.strptime(self.birth_date, "%Y-%m-%d")
        return f"({self.role}) {self.firstname} {self.lastname}. Birth date: {date.strftime('%d %B %Y')}"
class UserBuilder:
    def __init__(self):
        self.role: str
        self.first_name: str
        self.last_name: str
        self.pesel: str
        self.password: str
        self.birth_date: datetime.date

    def set_role(self, role: str) -> "UserBuilder":
        if role not in ["student", "wykladowca", "admin"]:
            raise ValueError("Invalid role. Allowed roles are: student, wykladowca, admin")
        self.role = role
        return self

    def set_first_name(self, first_name: str = "") -> "UserBuilder":
        self.first_name = first_name
        return self

    def set_last_name(self, last_name: str = "") -> "UserBuilder":
        self.last_name = last_name
        return self

    def set_pesel(self, pesel: str) -> "UserBuilder":
        self.pesel = pesel
        return self

    def set_password(self, password: str) -> "UserBuilder":
        self.password = password
        return self

    def set_birth_date(self, birth_date: datetime.date) -> "UserBuilder":
        self.birth_date = birth_date
        return self

    def build(self) -> User:
        if not all([self.role, self.first_name, self.last_name, self.pesel, self.password, self.birth_date]):
            raise ValueError("All fields must be set before building the user")

        return User(self.role, self.first_name, self.last_name, self.pesel, self.password, self.birth_date)


# Klasa książki oraz grupa książek autora (Composite)
class Component(ABC):
    @abstractmethod
    def display(self) -> None:
        pass
class Book(Component):
    def __init__(self, title: str, author: str, isbn: str, publication_year: int, genre: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.genre = genre

    def __str__(self):
        return f"({self.isbn}) {self.title} - {self.author} ({self.publication_year})"

    def display(self) -> None:
        print(f'"{self.title}" by {self.author} ({self.publication_year} year) - {self.genre}')
class AuthorGroup(Component):
    def __init__(self, author: str):
        self.author = author
        self.books: List[Component] = []

    def add(self, book: Component) -> None:
        self.books.append(book)

    def display(self) -> None:
        print(f"\nBooks by {self.author}:")
        for book in self.books:
            book.display()

# Klasa biblioteki do przechowywania i wyświetlania książek po autorach w uporządkowany sposób
class Library:
    def __init__(self):
        self.books = []
        self.authors_groups: Dict[str, AuthorGroup] = {}

    def add_books(self, books: list[Book]) -> None:
        for book in books:
            self.books.append(book)
            # Grupowanie książek po autorze
            if book.author not in self.authors_groups:
                self.authors_groups[book.author] = AuthorGroup(book.author)
            self.authors_groups[book.author].add(book)

    def display_books_by_author(self) -> None:
        for author_group in self.authors_groups.values():
            author_group.display()

# Mock bazy danych (Singleton)
class Database:
    # Seed wstępnych danych
    users: list = [
        User("student","Anna","Kowalska","92040512345","Anna123!","1992-04-05"),
        User("wykladowca","Jan","Nowak","88061354321","Janek88@","1988-06-13")
    ]
    books: list = [
        Book("Lalka", "Bolesław Prus", "9788306031234", 1890, "Powieść realistyczna"),
        Book("Zbrodnia i kara", "Fiodor Dostojewski", "9780140449136", 1866, "Powieść psychologiczna"),
        Book("Pan Tadeusz", "Adam Mickiewicz", "9788373271890", 1834, "Epopeja narodowa"),
        Book("Hobbit", "J.R.R. Tolkien", "9780261103344", 1937, "Fantasy"),
        Book("Mały Książę", "Antoine de Saint-Exupéry", "9780156012195", 1943, "Baśń filozoficzna"),
        Book("Władca Pierścieni", "J.R.R. Tolkien", "978026110330", 1954, "Fantasy")
    ]

    # kontruktor zapewniający, że nie powstanie druga instancja klasy Database
    _instance: Self = None
    def __new__(cls, *args: list, **kwargs: dict) -> Self:
        if cls._instance is None:
            instance = super().__new__(cls, *args, **kwargs)
            cls._instance = instance

        return cls._instance

    # Pobranie listy książek z bazy jeśli spełniamy warunki dekoratora odnośnie posiadania roli
    # Zwróci błąd również jeśli nie jesteśmy "zalogowani"
    @Access_check(["student", "wykladowca", "admin"])
    def get_books(self, user=None) -> list:
        return self.books

    # Login po peselu i haśle, jeśli udany to zwraca odpowiedniego użytkonika
    def login(self, pesel: str, password: str) -> User | None:
        for user in self.users:
            if user.pesel == pesel and user.password == password:
                return user
        print("Login failed")
        return None

    # Rejestracja wykorzystująca UserBuildera do utworzenia użytkownika krok po kroku
    def register(self, firstname:str, lastname:str, pesel:str, password:str, birth_date: datetime.date) -> None:
        if pesel in self.users:
            print("User already registered")

        userBuilder = UserBuilder()
        user = (userBuilder.set_role("student").set_first_name(firstname).set_last_name(lastname).set_pesel(pesel)
                .set_password(password).set_birth_date(birth_date).build())
        self.users.append(user)
        print("User registered")


# Połączenie z bazą (powiedzmy)
database = Database()

database.register("Robert", "Kochański", "99072605150", "password", "1999-07-26")
user = database.login("99072605150", "password")
print(user)

# Pobieranie z bazy wszystkich książek pod warunkiem, że użytkownik spełnia wymagania odnośnie roli
books = database.get_books(user=user)
for book in books:
    print(book)

# Wyświetlanie książek poukładanych według autora
library = Library()
library.add_books(books)
library.display_books_by_author()

# def main(name: str):
#     print(f"Hello {name}")
#
# if __name__ == "__main__":
#     typer.run(main)