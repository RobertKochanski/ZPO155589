from abc import ABC, abstractmethod

class Seq:
    macros: list[str]

    def __init__(self):
        self.macros = []

    def write(self, text: str):
        self.macros.append(text)
        print(f"Added {text} to macro sequence: {self.macros}")

    def delete(self):
        self.macros.pop()
        print(f"After delete last macro from sequence: {self.macros}")

    def reset(self):
        self.macros = []
        print("Sequence reset.")


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass

class WriteCommand(Command):
    seq: Seq
    text: str

    def __init__(self, seq: Seq, text: str) -> None:
        self.seq = seq
        self.text = text

    def execute(self) -> None:
        self.seq.write(self.text)

    def undo(self) -> None:
        for _ in self.text:
            self.seq.delete()

class DeleteCommand(Command):
    seq: Seq
    deleted_macro: str

    def __init__(self, seq: Seq) -> None:
        self.seq = seq
        self.deleted_macro = ""

    def execute(self) -> None:
        if self.seq.macros:
            self.deleted_macro = self.seq.macros[-1]
        self.seq.delete()

    def undo(self) -> None:
        if self.deleted_macro:
            self.seq.write(self.deleted_macro)


class MacroRecorder:
    seq: Seq
    macros: list[str]
    history: list[str]

    def __init__(self, seq: Seq) -> None:
        self.seq: Seq = seq
        self.macro = []
        self.history = []

    def record_macro(self, command):
        self.macro.append(command)

    def play_macro(self):
        self.history = []
        self.seq.reset()
        print("\nPlay macros:")
        for command in self.macro:
            command.execute()
            self.history.append(command)

    def undo_last(self):
        if self.history:
            print("\nUndoing last command:")
            last_command = self.history.pop()
            last_command.undo()

            self.macro.pop()
        else:
            print("\nNo commands to undo.")

    def read_macro(self):
        for macro in self.seq.macros:
            print(macro)

    def clear_macro(self):
        self.macro = []


seq = Seq()
recorder = MacroRecorder(seq)

recorder.record_macro(WriteCommand(seq, "GET Value"))
recorder.record_macro(WriteCommand(seq, "CREATE"))
recorder.record_macro(WriteCommand(seq, "DATA"))
recorder.record_macro(DeleteCommand(seq))
recorder.record_macro(WriteCommand(seq, "!"))

# recorder.clear_macro()

recorder.play_macro()
recorder.read_macro()

recorder.undo_last()
recorder.undo_last()

recorder.play_macro()
recorder.read_macro()