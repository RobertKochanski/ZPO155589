from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def whatAnimal(self) -> None:
        pass

class Dog(Animal):
    def whatAnimal(self) -> str:
        return "Dogge"

class Cat(Animal):
    def whatAnimal(self) -> str:
        return "Koteł"

class AnimalFactory:
    animalList = {"Dog": Dog, "Cat": Cat}

    def addAnimalToList(self, animalType:str, animal:Animal) -> None:
        self.animalList[animalType] = animal

    def createAnimal(self, animal:str) -> Animal:
        if animal in self.animalList:
            return self.animalList[animal]()
        raise ValueError


    # Statyczna instrucja
    # def createAnimal(self, name:str) -> Animal:
    #     if name == "Dog":
    #         return Dog()
    #     if name == "Cat":
    #         return Cat()
    #
    #     raise ValueError

# factory = AnimalFactory()
# dog = factory.createAnimal("Dog")
# print(dog.whatAnimal())


factory = AnimalFactory()

doggo = factory.createAnimal("Dog")
cat = factory.createAnimal("Cat")

print(doggo.whatAnimal())
print(cat.whatAnimal())