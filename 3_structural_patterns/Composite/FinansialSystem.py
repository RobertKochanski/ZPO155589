from abc import ABC, abstractmethod

class Report(ABC):
    @abstractmethod
    def display(self, depth=0) -> None:
        pass

class SingleValue(Report):
    value:float

    def __init__(self, value:float):
        self.value = value

    def display(self, depth=0) -> None:
        print("  " * depth + f"- {self.value}")

class Section(Report):
    name:str
    elements:list[Report]

    def __init__(self, name:str):
        self.name = name
        self.elements = []

    def add(self, element:Report) -> None:
        self.elements.append(element)

    def display(self, depth=0) -> None:
        print("  " * depth + f"- {self.name}")
        for element in self.elements:
            element.display(depth + 1)


value1 = SingleValue(10)
value2 = SingleValue(20)

section1 = Section("section1")
section2 = Section("section2")

section1.add(value1)
section2.add(value2)
section1.add(section2)

section1.display()