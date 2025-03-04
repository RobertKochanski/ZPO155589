from abc import ABC, abstractmethod
from typing import Self


class Pizza:
    def __init__(self):
        self.ingredients = []


class PizzaBuilder():
    def __init__(self):
        self.pizza = Pizza()

    def addCheese(self) -> Self:
        self.pizza.ingredients.append("Cheese")
        return self

    def addSalami(self) -> Self:
        self.pizza.ingredients.append("Salami")
        return self

    def addMushroom(self) -> Self:
        self.pizza.ingredients.append("Mushroom")
        return self

    def addOnion(self) -> Self:
        self.pizza.ingredients.append("Onion")
        return self

    def addCorn(self) -> Self:
        self.pizza.ingredients.append("Corn")
        return self

    def addPeppers(self) -> Self:
        self.pizza.ingredients.append("Peppers")
        return self

    def addPineapple(self) -> Self:
        self.pizza.ingredients.append("Pineapple")
        return self

    def resetIngredients(self) -> None:
        self.pizza.ingredients.clear()

    def show_current_ingredients(self) -> Self:
        print(self.pizza.ingredients)
        return self

    def build(self) -> Pizza:
        return self.pizza

class PizzaDirector:
    def createPizza(self) -> Pizza:
        return PizzaBuilder().addCheese().addSalami().build()

    def createVegePizza(self) -> Pizza:
        return PizzaBuilder().addCheese().addCorn().addOnion().build()

    def createMeatPizza(self) -> Pizza:
        return PizzaBuilder().addCheese().addSalami().addPeppers().build()


director = PizzaDirector()
Pepperoni = director.createPizza()

print(Pepperoni.ingredients)

