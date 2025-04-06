class FormState:
    size: list
    firstname: str
    lastname: str

    def __init__(self, size: list, firstname: str, lastname: str) -> None:
        self.size = size
        self.firstname = firstname
        self.lastname = lastname

class Memento:
    _states: list
    _i: int

    def __init__(self) -> None:
        self._states = []
        self._i: int = -1

    def save_state(self, state: FormState) -> None:
        if self._i != len(self._states) - 1:
            self._states = self._states[:self._i + 1]

        self._states.append(state)
        self._i += 1

    def undo(self) -> None:
        if self._i > 0:
            self._i -= 1

    def redo(self) -> None:
        if self._i < len(self._states) - 1:
            self._i += 1

    def read_state(self) -> FormState:
        return self._states[self._i]

class Form:
    size: list
    firstname: str
    lastname: str
    memento: Memento

    def __init__(self, size: list, firstname: str, lastname: str) -> None:
        self.size = size
        self.firstname = firstname
        self.lastname = lastname
        self.memento = Memento()

    def __str__(self):
        return f'{self.size}: {self.firstname} {self.lastname}'

    def change_data(self, size: list, firstname: str, lastname: str):
        self.size = size
        self.firstname = firstname
        self.lastname = lastname

    def save_state(self):
        state = FormState(self.size, self.firstname, self.lastname)
        self.memento.save_state(state)

    def undo(self):
        self.memento.undo()
        state = self.memento.read_state()
        self.size = state.size
        self.firstname = state.firstname
        self.lastname = state.lastname

    def redo(self):
        self.memento.redo()
        state = self.memento.read_state()
        self.size = state.size
        self.firstname = state.firstname
        self.lastname = state.lastname


form = Form([1024, 680], "firstname", "lastname")
print(form)
form.save_state()

form.change_data([2048, 1248], "changed firstname", "lastname")
print(form)
form.save_state()

form.undo()
print(form)

form.redo()
print(form)
