import datetime

from rich import print

from Project.LogicLayer.Books import Book
from Project.LogicLayer.Interfaces.Observer import Observer


class User(Observer):
    role: str = ""
    firstname: str = ""
    lastname: str = ""
    pesel: str = ""
    password: str = ""
    birth_date: datetime.date = None

    def __init__(self):
        self.operation_hist: list = []

    def __str__(self):
        return f"({self.role}) {self.firstname} {self.lastname}."

    def notify(self, book: Book) -> None:
        print("[yellow]\nReservation Notice:[/yellow]")
        print(f"Hey, [green_yellow]{self.firstname} {self.lastname}[/green_yellow], book '{book.title}' is now available!")

class UserBuilder:
    user: User

    errors: int = 0

    def __init__(self):
        self.user = User()

    def set_role(self, role: str = "Student") -> "UserBuilder":
        if role not in ["Student", "Teacher", "Admin"]:
            self.errors += 1
            print("[red]Invalid role. Allowed roles are: Student, Teacher, Admin[/red]")
        self.user.role = role
        return self

    def set_first_name(self, firstname: str = "") -> "UserBuilder":
        self.user.firstname = firstname
        return self

    def set_last_name(self, lastname: str = "") -> "UserBuilder":
        self.user.lastname = lastname
        return self

    def set_pesel(self, pesel: str = "") -> "UserBuilder":
        if not pesel.isdigit() or len(pesel) != 11:
            self.errors += 1
            print("[yellow]PESEL must be 11 digits[/yellow]")
        self.user.pesel = pesel
        return self

    def set_password(self, password: str = "") -> "UserBuilder":
        if len(password) < 5:
            self.errors += 1
            print("[yellow]Password must be at least 5 characters[/yellow]")
        self.user.password = password
        return self

    def set_birth_date(self, birth_date: str) -> "UserBuilder":
        try:
            birth_date_obj = datetime.datetime.strptime(birth_date, "%d-%m-%Y").date()
            self.user.birth_date = birth_date_obj
        except ValueError as e:
            self.errors += 1
            print(f"[yellow]Wrong date format: {e}. Expected format: DD-MM-YYYY[/yellow]")
        return self

    def build(self) -> User:
        if not all([self.user.firstname, self.user.lastname, self.user.role, self.user.pesel, self.user.password, self.user.birth_date]):
            self.errors += 1
            print("[yellow]All required fields must be set before building the user[/yellow]")

        if self.errors > 0:
            raise ValueError

        built_user = self.user
        self.user = User()

        return built_user