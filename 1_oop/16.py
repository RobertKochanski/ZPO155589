# ========= Zadanie 16 =============
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> None:
        pass

class Circle(Shape):
    def area(self) -> str:
        return "Area of circle"

class Rectangle(Shape):
    def area(self) -> str:
        return "Area of rectangle"

print(Circle().area())
print(Rectangle().area())