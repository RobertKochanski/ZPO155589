import os

import typer
from typer.rich_utils import Table, Align
from rich.prompt import Prompt, Confirm
from rich import print

from Project.LogicLayer.Books.AuthorGroup import AuthorGroup
from Project.LogicLayer.Books.Book import Book
from Project.LogicLayer.DbContext import Database
from Project.LogicLayer.Strategies.BorrowStrategy import ShortTermBorrowStrategy, NormalTermBorrowStrategy, LongTermBorrowStrategy
from Project.Console_app import user_state


app = typer.Typer()
db = Database()

@app.command()
def main():
    while True:
        # Jeśli użytkownik nie jest zalogowny, wyświetlamy menu logowania
        if user_state.current_user is None:
            show_login_menu()
            login_action = Prompt.ask("Choose an option[cyan](1-3)[/cyan]")
            os.system('cls' if os.name == 'nt' else 'clear')

            match login_action:
                # 1. odpowiada za logowanie użytkownika do aplikacji
                case "1":
                    login()
                # 2. odpowiada za rejestrację użytkownika w aplikacji
                case "2":
                    register()
                # 0. odpowiada za wyłączenie aplikacji
                case "0":
                    user_state.current_user = None
                    print("[cyan]See you later :smile::hand: [/cyan]")
                    break
                case _:
                    print("[red]Invalid input.[/red]")
        # Jeśli użytkownik jest zalogowany, wyświetlamy możliwe operacje
        else:
            show_operations_menu(f"Logged in as: [yellow]{user_state.current_user.firstname} {user_state.current_user.lastname}[/yellow]")
            operation = Prompt.ask("Choose an option")
            os.system('cls' if os.name == 'nt' else 'clear')

            match operation:
                # 1. odpowiada za wyświetlanie książek posortowanych po nazwie w formie tabeli
                case "1":
                    books = db.get_books()
                    print_books_table(books, "List of books")
                # 1a. odpowiada za wyświetlanie książek poukładanych w postaci autor - jego książki w formie tabeli
                case "1a":
                    books = db.get_books()
                    print_books_by_author(books)
                # 2. odpowiada za wyświetlanie swoich wypożyczeń
                case "2":
                    borrows = db.show_borrowed(user = user_state.current_user)

                    if borrows is not None:
                        print_borrows_table(borrows, "Your borrows")
                # 3. odpowiada za wypożyczenie książki po isbn
                case "3":
                    borrow_book()
                # 4. odpowiada za zwracanie książki
                case "4":
                    borrows = db.show_borrowed(user = user_state.current_user)

                    if borrows is not None:
                        print_borrows_table(borrows, "Your borrows")
                        isbn = Prompt.ask("ISBN: ")
                        db.return_book(isbn, user=user_state.current_user)
                # 5. odpowiada za rezerwację książki
                case "5":
                    isbn = Prompt.ask("ISBN: ")
                    db.reserve_book(isbn, user=user_state.current_user)
                # 6. odpowiada za wyświetlenie historii operacji
                case "6":
                    show_history()
                # 7. odpowiada za cofnięcie ostatniej operacji (wypożyczenie, zwrot)
                case "7":
                    undo_operation()
                # 8. odpowiada za dodawnie książek przez nauczycieli i adminów (studenci nie mają dostępu)
                case "8":
                    add_book()
                # 8a. odpowiada za edytowanie istniejącej książki (studenci nie mają dostępu)
                case "8a":
                    edit_book()
                # 8b. odpowiada za usuwanie istniejącej książki (studenci nie mają dostępu)
                case "8b":
                    delete_book()
                # 999. odpowiada za przetestowanie funkcjonalności powiadomień zarezerwowanych książek przy ich zwrocie
                case "999":
                    reservation_return_simulation()
                # 9. odpowiada za wylogowanie się z aplikacji ale bez jej wyłączania
                case "9":
                    print("[yellow]Logged out[/yellow]")
                    user_state.current_user = None
                # 0. odpowiada za wylogowanie się z aplikacji oraz jej wyłączeniu
                case "0":
                    print("[cyan]See you later :smile::hand: [/cyan]")
                    user_state.current_user = None
                    break
                case _:
                    print("[yellow]Not allowed operation[/yellow]")



def show_login_menu() -> None:
    login_table = Table()
    login_table.add_column("[green]### MENU ###[/green]")
    login_table.add_row("1. Login")
    login_table.add_row("2. Register")
    login_table.add_row("0. [red]Exit[/red]")

    print(login_table)
def show_operations_menu(title:str) -> None:
    print()
    operations_table = Table(title=title)
    operations_table.add_column(f"[green]### What would you like do to Mr/Ms [yellow]{user_state.current_user.lastname}[/yellow]? ###[/green]")
    operations_table.add_row("1.    Check books")
    operations_table.add_row("1a.   Check books sorted by author")
    operations_table.add_row("2.    Check your borrows")
    operations_table.add_row("3.    Borrow book [steel_blue1](need book's isbn)[/steel_blue1]")
    operations_table.add_row("4.    Return borrowed book")
    operations_table.add_row("5.    Reservation book [steel_blue1](need book's isbn)[/steel_blue1]")
    operations_table.add_row("6.    Show operations history")
    operations_table.add_row("7.    Undo last operation")
    if user_state.current_user.role != "Student":
        operations_table.add_row("8.    Add book [indian_red](only for teachers/admins)[/indian_red]")
        operations_table.add_row("8a.   Edit book [indian_red](only for teachers/admins)[/indian_red]")
        operations_table.add_row("8b.   Delete book [indian_red](only for teachers/admins)[/indian_red]")
    operations_table.add_row("9.    Logout.", style="yellow")
    operations_table.add_row("0.    Exit", style="red")
    operations_table.add_row()
    operations_table.add_row("999.  Reserve notification - test", style="magenta")

    print(operations_table)

def print_books_table(books: list[Book], title: str) -> None:
    table = Table(title=title)

    table.add_column("Isbn", style="cyan")
    table.add_column("Title", style="magenta")
    table.add_column("Author", style="green")
    table.add_column("Genre", style="yellow")
    table.add_column("Publication year", justify="right")
    table.add_column("Is available", justify="center")

    borrowed_books = [borrow.book for borrow in db.borrows]

    for book in books:
        is_available = ":white_check_mark:" if book not in borrowed_books else ":x:"

        table.add_row(
            book.isbn,
            book.title,
            book.author,
            book.genre,
            str(book.publication_year),
            is_available,
        )

    print(Align.center(table))
def print_books_by_author(books: list[Book]) -> None:
    author_groups: list[AuthorGroup] = []

    # dla każdej książki szukamy grupy, jeśli grupa nie istnieje, tworzona jest nowa i dodawana do listy
    for book in sorted(books, key=lambda b: b.title):
        group = next((author_group for author_group in author_groups if author_group.author == book.author), None)
        if not group:
            group = AuthorGroup(book.author)
            author_groups.append(group)
        group.add(book)

    table = Table(title="List of Books by Author")

    table.add_column("Author", style="green")
    table.add_column("Isbn", style="cyan")
    table.add_column("Title", style="magenta")
    table.add_column("Genre", style="yellow")
    table.add_column("Publication year", justify="right")
    table.add_column("Is available", justify="center")

    borrowed_books = [borrow.book for borrow in db.borrows]

    for author_group in sorted(author_groups, key=lambda author_group: author_group.author):
        for row in author_group.to_table():
            if not row[0]:
                if db.get_book_by_isbn(row[1]) not in borrowed_books:
                    is_available = ":white_check_mark:"
                else:
                    is_available = ":x:"
            else:
                is_available = None
            table.add_row(row[0], row[1], row[2], row[3], row[4], is_available)

    print(Align.center(table))
def print_borrows_table(borrows , title: str) -> None:
    table = Table(title=title)

    table.add_column("Isbn", style="cyan")
    table.add_column("Title", style="magenta")
    table.add_column("Author", style="green")
    table.add_column("Genre", style="yellow")
    table.add_column("Publication year", justify="right")
    table.add_column("Borrowed", justify="right", style="turquoise2")
    table.add_column("Borrowed until", justify="right", style="green1")

    for borrow in borrows:
        table.add_row(
            borrow.book.isbn,
            borrow.book.title,
            borrow.book.author,
            borrow.book.genre,
            str(borrow.book.publication_year),
            str(borrow.borrow_date),
            str(borrow.borrowed_until_date),
        )

    print(Align.center(table))

def login() -> None:
    print("1. Login")
    pesel = Prompt.ask("Pesel: ")
    password = Prompt.ask("Password: ", password=True)
    os.system('cls' if os.name == 'nt' else 'clear')
    user = db.login(pesel, password)
    if user:
        user_state.current_user = user
def register() -> None:
    print("2. Register")
    firstname: str = Prompt.ask("First name[red]*[/red]: ")
    lastname: str = Prompt.ask("Last name[red]*[/red]: ")
    pesel = Prompt.ask("Pesel[red]*[/red]: ")
    password = Prompt.ask("Password[red]*[/red] [yellow](at least 5 characters)[/yellow]: ", password=True)
    birth_date = Prompt.ask("Birth date (dd-mm-yyyy)[red]*[/red]: ")
    os.system('cls' if os.name == 'nt' else 'clear')

    db.register(firstname.capitalize(), lastname.capitalize(), pesel, password, birth_date)

def add_book() -> None:
    if "Student" == user_state.current_user.role:
        print("[yellow]Not allowed operation[/yellow]")
    else:
        print("[light_slate_blue]Make sure you did not make a [red1]mistake[/red1], thanks.[/light_slate_blue]")
        title = Prompt.ask("Title ")
        author = Prompt.ask("Author ")
        isbn = Prompt.ask("ISBN ")
        publication_year = Prompt.ask("Publication year ")
        genre = Prompt.ask("Genre ")
        new_book = Book(title, author, isbn, int(publication_year), genre)

        db.add_book(new_book, user=user_state.current_user)
def edit_book() -> None:
    if "Student" == user_state.current_user.role:
        print("[yellow]Not allowed operation[/yellow]")
    else:
        isbn = Prompt.ask("ISBN: ")

        if not db.get_book_by_isbn(isbn):
            print(f"[red]Book ({isbn}) not found.[/red]")
        else:
            to_change: dict = {}
            author_change = Confirm.ask("Do you want to change your book's author?")
            if author_change:
                new_author = Prompt.ask("New author")
                if new_author != "":
                    to_change["author"] = new_author

            title_change = Confirm.ask("Do you want to change your book's title?")
            if title_change:
                new_title = Prompt.ask("New title")
                if new_title != "":
                    to_change["title"] = new_title

            publication_year_change = Confirm.ask("Do you want to change your book's publication year?")
            if publication_year_change:
                new_publication_year = Prompt.ask("New publication year")
                if new_publication_year != "":
                    to_change["publication_year"] = new_publication_year

            genre_change = Confirm.ask("Do you want to change your book's genre?")
            if genre_change:
                new_genre = Prompt.ask("New genre")
                if new_genre != "":
                    to_change["genre"] = new_genre

            if to_change:
                db.edit_book(isbn, to_change, user=user_state.current_user)
            else:
                print("[yellow]Changes not detected[/yellow]")
def delete_book() -> None:
    if "Student" == user_state.current_user.role:
        print("[yellow]Not allowed operation[/yellow]")
    else:
        isbn = Prompt.ask("ISBN: ")
        book = db.get_book_by_isbn(isbn)
        if book:
            confirm = Confirm.ask(f"You are going to delete [magenta]'{book.title}' - {book.author}[/magenta]. Confirm?")
            if confirm:
                db.remove_book(isbn, user=user_state.current_user)
        else:
            print(f"[red]Book ({isbn}) not found.[/red]")

def borrow_book() -> None:
    isbn = Prompt.ask("ISBN: ")

    book = db.get_book_by_isbn(isbn)
    if not book:
        print(f"[red]Book ({isbn}) not found.[/red]")
        return

    user_strategy: str = Prompt.ask("Choose borrow term: \n1. Short ([cyan]7 days[/cyan])\n"
                                    "2. Standard ([cyan]14 days[/cyan])\n3. Long ([cyan]30 days[/cyan])")
    if user_strategy == "1":
        strategy = ShortTermBorrowStrategy()
        db.borrow_book(isbn, strategy, user=user_state.current_user)
    elif user_strategy == "2":
        strategy = NormalTermBorrowStrategy()
        db.borrow_book(isbn, strategy, user=user_state.current_user)
    elif user_strategy == "3":
        strategy = LongTermBorrowStrategy()
        db.borrow_book(isbn, strategy, user=user_state.current_user)
    else:
        print("[red]Invalid input.[/red]")
def undo_operation() -> None:
    if user_state.current_user.operation_hist:
        last_operation: dict | None = user_state.current_user.operation_hist[-1]
    else:
        last_operation: dict | None = None

    if not last_operation:
        print("[red]No operation to undo[/red]")
        return

    if last_operation["type"] == "borrow":
        db.return_book(last_operation["isbn"], user=user_state.current_user)
    elif last_operation["type"] == "return":
        print("You want to borrow your last returned book.")
        user_strategy: str = Prompt.ask("Choose borrow term again: \n1. Short ([cyan]7 days[/cyan])\n"
                                        "2. Standard ([cyan]14 days[/cyan])\n3. Long ([cyan]30 days[/cyan])")
        if user_strategy == "1":
            strategy = ShortTermBorrowStrategy()
            db.borrow_book(last_operation["isbn"], strategy, user=user_state.current_user)
        elif user_strategy == "2":
            strategy = NormalTermBorrowStrategy()
            db.borrow_book(last_operation["isbn"], strategy, user=user_state.current_user)
        elif user_strategy == "3":
            strategy = LongTermBorrowStrategy()
            db.borrow_book(last_operation["isbn"], strategy, user=user_state.current_user)
        else:
            print("[red]Invalid input.[/red]")
def show_history() -> None:
    if user_state.current_user.operation_hist:
        table = Table(title="Your operations history")
        table.add_column("Date", justify="right")
        table.add_column("Operation type", style="green")
        table.add_column("Book's isbn", style="cyan", justify="right")

        for operation in sorted(user_state.current_user.operation_hist, key=lambda x: x["date"], reverse=True):
            table.add_row(operation["date"], operation["type"], operation["isbn"])

        print(table)
    else:
        print("[red]No operation to show[/red]")
def reservation_return_simulation() -> None:
    temp_user = db.login("12312312312", "password") # User(Robert, Admin)

    print("[red]SIMULATION (You need to be logged in different account than admin):[/red]")
    # Borrow "Zbrodnia i kara" by temp_user
    print("[cyan]1. Another user borrowed book 'Zbrodnia i kara'[/cyan]")
    db.borrow_book("9788373273122", LongTermBorrowStrategy(), user = temp_user)

    # Reserve "Zbrodnia i kara" by current user
    print("[cyan]2. Logged user reservated book 'Zbrodnia i kara'[/cyan]")
    db.reserve_book("9788373273122", user = user_state.current_user)

    # temp_user return book
    print("[cyan]3. Another user returned book 'Zbrodnia i kara'[/cyan]")
    db.return_book("9788373273122", user = temp_user)

if __name__ == "__main__":
    app()