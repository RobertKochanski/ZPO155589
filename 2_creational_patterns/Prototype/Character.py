from dataclasses import dataclass
from abc import ABC, abstractmethod
from copy import deepcopy, copy
from typing import Any

class Character_type(ABC):
    @abstractmethod
    def what_type(self) -> None:
        pass

class Mage(Character_type):
    def __init__(self):
        self.class_type = "Warrior"

    def what_type(self) -> str:
        return "Im a mage"

class Warrior(Character_type):
    def __init__(self):
        self.class_type = "Warrior"

    def what_type(self) -> str:
        return "Im a warrior"

@dataclass
class Character:
    name: str
    hp: int
    dmg: float
    class_type: Character_type

class CharacterPrototype:
    def clone(self, object:Any) -> Any:
        return deepcopy(object)


prototype = CharacterPrototype()

warrior = Character("name", 100, 10.0, Warrior())

warrior_shallow = copy(warrior)
warrior_shallow.dmg = 20.0
warrior_deep = prototype.clone(warrior)

print(f"Warrior: {warrior}")
print(f"Warrior shallow clone: {warrior_shallow}")
print(f"Warrior deep clone: {warrior_deep}")

print("Shallow clone references: " + f"{warrior == warrior_shallow}")
print("Shallow clone references class_type: " + f"{warrior.class_type == warrior_shallow.class_type}")

print("Deep clone references: " + f"{warrior == warrior_deep}")
print("Deep clone references class_type: " + f"{warrior.class_type == warrior_deep.class_type}")

