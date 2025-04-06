class Memento:
    _states: list
    _i: int

    def __init__(self) -> None:
        self._states = []
        self._i: int = -1

    def save_state(self, state: list[int, bool]) -> None:
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

    def read_state(self) -> list[int, bool]:
        return self._states[self._i]

class Settings:
    def __init__(self, font_size: int, dark_mode: bool) -> None:
        self.memento = Memento()
        self.change_settings(font_size, dark_mode)

    def __str__(self):
        return f"font_size: {self.font_size}, dark_mode: {self.dark_mode}"

    def change_settings(self, font_size: int, dark_mode: bool) -> None:
        self.font_size = font_size
        self.dark_mode = dark_mode
        self.memento.save_state([self.font_size, self.dark_mode])

    def undo(self):
        self.memento.undo()
        self.font_size, self.dark_mode = self.memento.read_state()

    def redo(self):
        self.memento.redo()
        self.font_size, self.dark_mode = self.memento.read_state()


settings = Settings(12, True)
print(settings)

settings.change_settings(16, False)
print("First change:", settings)

settings.change_settings(20, True)
print("Second change:", settings)

settings.undo()
print("After undo:", settings)

settings.undo()
print("Again after undo:", settings)

settings.change_settings(10, False)
print("Test:", settings)

settings.redo()
print("After redo:", settings)
