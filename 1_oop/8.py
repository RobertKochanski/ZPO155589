# ========= Zadanie 8 =============
class Animal:
    def make_sound(self):
        return "Some sound"

class Pet:
    def is_domestic(self):
        return True

class Dog(Animal, Pet):
    def make_sound(self):
        return "Hau"
    def is_domestic(self):
        return True

print(Animal().make_sound())
print(Pet().is_domestic())
print(Dog().make_sound(), Dog().is_domestic())