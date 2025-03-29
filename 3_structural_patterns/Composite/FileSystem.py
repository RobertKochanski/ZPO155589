from typing import Any
from abc import ABC, abstractmethod

class FileSystem(ABC):
    @abstractmethod
    def display(self, depth:int = 0) -> None:
        pass

class File(FileSystem):
    name:str
    extension:str

    def __init__(self, name:str, extension:str):
        self.name = name
        self.extension = extension

    def display(self, depth=0) -> None:
        print("  " * depth + f"- {self.name}.{self.extension}")


class Directory(FileSystem):
    name:str
    elements: list[FileSystem]

    def __init__(self, name:str):
        self.name = name
        self.elements = []

    def add(self, element:FileSystem) -> None:
        self.elements.append(element)

    def display(self, depth=0) -> None:
        print("  " * depth + f"- {self.name}")
        for element in self.elements:
            element.display(depth + 1)


root_dic = Directory("home")
file1 = File("file1", "txt")
file2 = File("file2", "txt")

dic = Directory("Directory")
file3 = File("file3", "txt")

root_dic.add(file1)
root_dic.add(file2)
root_dic.add(dic)
dic.add(file3)

root_dic.display()