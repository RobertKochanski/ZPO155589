class Pizza:
    def __init__(self):
        self.ingredients = []

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def addCheese(self):
        self.pizza.ingredients.append("Cheese")
        return self

    def addSalami(self):
        self.pizza.ingredients.append("Salami")
        return self

    def addMushroom(self):
        self.pizza.ingredients.append("Mushroom")
        return self

    def addOnion(self):
        self.pizza.ingredients.append("Onion")
        return self

    def resetIngredients(self) -> None:
        self.pizza.ingredients.clear()

    def show_current_ingredients(self):
        print(self.pizza.ingredients)
        return self

    def build(self) -> Pizza:
        return self.pizza

pizza = PizzaBuilder().addSalami().addOnion().addCheese().show_current_ingredients().build()
print(pizza.ingredients)

class NotPizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def addPineapple(self):
        self.pizza.ingredients.append("Pineapple")
        return self

    def build(self) -> Pizza:
        return self.pizza


notPizza = NotPizzaBuilder().addPineapple().build()
print(notPizza.ingredients)

class VegePizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def addTofu(self):
        self.pizza.ingredients.append("Tofu")
        return self
    def addVegeCheese(self):
        self.pizza.ingredients.append("VegeCheese")
        return self
    def addMushrooms(self):
        self.pizza.ingredients.append("Mushrooms")
        return self
    def addCorn(self):
        self.pizza.ingredients.append("Corn")
        return self
    def addPeppers(self):
        self.pizza.ingredients.append("Peppers")
        return self

    def build(self) -> Pizza:
        return self.pizza


vegePizza = VegePizzaBuilder().addVegeCheese().addCorn().addTofu().addPeppers().build()
print(vegePizza.ingredients)