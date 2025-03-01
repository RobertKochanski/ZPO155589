import datetime
from collections import namedtuple
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from pydantic import BaseModel, Field
from datetime import datetime # zadanie 5


# ========= Zadanie 1 =============
class Employee:
    first_name: str
    last_name: str
    salary: float

    def __init__(self, first_name:str, last_name:str, salary:float):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self) -> str:
        return f"{self.first_name + ' ' + self.last_name}"


class Manager(Employee):
    department: str

    def __init__(self, first_name:str, last_name:str, salary:float, department:str):
        super().__init__(first_name, last_name, salary)
        self.department = department

    def get_department_info(self) -> str:
        return self.department

# employee = Employee("Jan", "Kowalski", 5000)
# print(employee.get_full_name())
#
# manager = Manager("Andrzej", "Nowak", 10000, "department")
# print(manager.get_full_name())
# print(manager.get_department_info())


# ========= Zadanie 2 =============
Transaction = namedtuple("Transaction", ["transaction_id", "amount", "currency"])

class BankAccount:
    balance: float

    def __init__(self, balance:float):
        self.balance = balance

    def apply_transaction(self, transaction: Transaction):
        self.balance += transaction.amount

# bankAccount = BankAccount(100)
# bankAccount.apply_transaction(Transaction(1, 10, "PLN"))
# print(bankAccount.balance)

# ========= Zadanie 3 =============
@dataclass()
class Book:
    title: str
    author: str
    year: int
    price: float

    def apply_discount(self, discount: int):
        self.price -=  round(self.price * discount / 100, 2)

# book = Book("title", "author", 1999, 9.99)
# book.apply_discount(50)
# print(book)

# ========= Zadanie 4 =============
@dataclass()
class Product:
    name:str
    price:float
    category:str = field(default="General")

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price >= 0")

# throw ValueError
# product = Product("name", -1)
# print(product)

# work properly
# product2 = Product("name2", 10)
# print(product2)

# ========= Zadanie 5 =============
@dataclass()
class Car:
    brand:str
    model:str
    year:int

    def is_classic(self) -> bool:
        return datetime.now().year - self.year > 25

# car = Car("Fiat", "Punto", 1999)
# print(car.is_classic())


# ========= Zadanie 6 =============
class ElectricVehicle:
    def fuel_type(self) -> str:
        return "electric"

class GasolineVehicle:
    def fuel_type(self) -> str:
        return "gasoline"

class HybridCar(ElectricVehicle, GasolineVehicle):
    def fuel_type(self) -> str:
        return "hybrid"

# print(ElectricVehicle().fuel_type())
# print(GasolineVehicle().fuel_type())
# print(HybridCar().fuel_type())

# ========= Zadanie 7 =============
class Person:
    def introduce(self) -> str:
        return "I am a person"

class Worker(Person):
    def introduce(self) -> str:
        return "I am a worker"

class Student(Person):
    def introduce(self) -> str:
        return "I am a student"

class WorkingStudent(Worker, Student):
    pass

# print(WorkingStudent.mro())

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

# print(Animal().make_sound())
# print(Pet().is_domestic())
# print(Dog().make_sound(), Dog().is_domestic())

# ========= Zadanie 9 =============
class FlyingVehicle:
    def move(self) -> str:
        return "I fly"

class WaterVehicle:
    def move(self) -> str:
        return "I sail"

class AmphibiousVehicle:
    mode:bool # 0-flying, 1-water

    def __init__(self, mode:bool):
        self.mode = mode

    def move(self) -> str:
        if self.mode == False:
            return "I fly"
        elif self.mode:
            return "I sail"
        else:
            return "Something went wrong"

# print(FlyingVehicle().move())
# print(WaterVehicle().move())
# print(AmphibiousVehicle(True).move())
# print(AmphibiousVehicle(False).move())

# ========= Zadanie 10 =============
class Robot:
    def operate(self) -> str:
        return "Performing task"

class AI:
    def think(self) -> str:
        return "Processing data"

class Android(Robot, AI):
    def self_learn(self) -> str:
        return "Self learning"

# print(Robot().operate())
# print(AI().think())
# print(Android().operate())
# print(Android().think())
# print(Android().self_learn())

# ========= Zadanie 11 =============
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius:float) -> float:
        return (9/5 * celsius) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit:float) -> float:
        return (fahrenheit - 32) * 5/9

# print(TemperatureConverter.celsius_to_fahrenheit(10))
# print(TemperatureConverter.fahrenheit_to_celsius(50))

# ========= Zadanie 12 =============
class IDGenerator:
    id: int = 0

    @classmethod
    def generate_id(cls) -> int:
        cls.id += 1
        return cls.id

# print(IDGenerator.generate_id())
# print(IDGenerator.generate_id())
# print(IDGenerator.generate_id())

# ========= Zadanie 13 =============
class Store:
    total_customers: int = 5

    @classmethod
    def add_customer(cls) -> None:
        cls.total_customers += 1

    @classmethod
    def get_total_customers(cls) -> int:
        return cls.total_customers

# print(Store.get_total_customers())
# Store.add_customer()
# print(Store.get_total_customers())

# ========= Zadanie 14 =============
class MathOperations:
    @staticmethod
    def add(a:float, b:float) -> float:
        return a + b

    @staticmethod
    def multiply(a:float, b:float) -> float:
        return a * b

    @classmethod
    def identity_matrix(cls, size:int) -> []:
        matrix = [[0]*size for i in range(size)]
        for j in range(size):
            matrix[j][j] = 1
        return matrix

# print(MathOperations.add(2, 3))
# print(MathOperations.multiply(2, 3))
# print(MathOperations.identity_matrix(3))

# ========= Zadanie 15 =============
class GameCharacter:
    default_health:int = 100

    def __init__(self):
        self.health = self.default_health

    def restore_health(self):
        self.health = GameCharacter.default_health

    @classmethod
    def set_default_health(cls, value):
        cls.default_health = value

# print(f"Default HP: {GameCharacter.default_health}")
# character1 = GameCharacter()
# character2 = GameCharacter()
# print(f"Character 1: {character1.health}")
# print(f"Character 2: {character2.health}")
# GameCharacter.set_default_health(150)
# print(f"Default HP (after change): {GameCharacter.default_health}")
# character1.restore_health()
# print(f"Character 1 (restored): {character1.health}")
# print(f"Character 2: {character2.health}")
# character3 = GameCharacter()
# print(f"Character 3: {character3.health}")

# ========= Zadanie 16 =============
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

# print(Circle().area())
# print(Rectangle().area())

# ========= Zadanie 17 =============
class PaymentProcessor(ABC):
    @abstractmethod
    def authorize_payment(self) -> None:
        pass

    @abstractmethod
    def capture_payment(self) -> None:
        pass

class CreditCardPayment(PaymentProcessor):
    def authorize_payment(self) -> str:
        return "Authorize credit card payment"

    def capture_payment(self) -> str:
        return "Capture credit card payment"


class PayPalPayment(PaymentProcessor):
    def authorize_payment(self) -> str:
        return "Authorize PayPal payment"

    def capture_payment(self) -> str:
        return "Capture PayPal payment"

# print(CreditCardPayment().authorize_payment())
# print(CreditCardPayment().capture_payment())
# print(PayPalPayment().authorize_payment())
# print(PayPalPayment().capture_payment())

# ========= Zadanie 18 =============
class Vehicle(ABC):
    @abstractmethod
    def max_speed(self) -> None:
        pass

class Car(Vehicle):
    def max_speed(self) -> float:
        return 400

class Bicycle(Vehicle):
    def max_speed(self) -> float:
        return 40

# print(Car().max_speed())
# print(Bicycle().max_speed())

# ========= Zadanie 19 =============
class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass
    def execute_query(self) -> None:
        pass

class MySQLConnection(DatabaseConnection):
    def connect(self) -> str:
        return "Connect to MySQL logic"
    def execute_query(self) -> str:
        return "Execute query MySQL logic"

class PostgreSQLConnection(DatabaseConnection):
    def connect(self) -> str:
        return "Connect to PostgreSQL logic"
    def execute_query(self) -> str:
        return "Execute query PostgreSQL logic"

# print(MySQLConnection().connect())
# print(MySQLConnection().execute_query())
# print(PostgreSQLConnection().connect())
# print(PostgreSQLConnection().execute_query())

# ========= Zadanie 20 =============
class Instrument(ABC):
    @abstractmethod
    def play(self) -> None:
        pass

class Piano(Instrument):
    def play(self) -> str:
        return "Piano play"

class Guitar(Instrument):
    def play(self) -> str:
        return "Guitar play"

print(Piano().play())
print(Guitar().play())
