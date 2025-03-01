# ========= Zadanie 8 =============
class Animal:
    def make_sound(self) -> str:
        return "Some sound"

class Pet:
    def is_domestic(self) -> bool:
        return True

class Dog(Animal, Pet):
    def make_sound(self) -> str:
        return "Hau"
    def is_domestic(self) -> bool:
        return True

print(Animal().make_sound())
print(Pet().is_domestic())
print(Dog().make_sound(), Dog().is_domestic())