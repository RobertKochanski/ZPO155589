import datetime
from collections import namedtuple
from dataclasses import dataclass
from pydantic import BaseModel, Field


# ========= Zadanie 1 =============
class Employee:
    first_name: str
    last_name: str
    salary: float

    def get_full_name(self):
        return f"{self.first_name + ' ' + self.last_name}"


class Manager(Employee):
    department: str

    def get_department_info(self):
        return self.department


# ========= Zadanie 2 =============
Transaction = namedtuple("Transaction", ["transaction_id", "amount", "currency"])

class BankAccount:
    balance: float

    def apply_transaction(self, transaction: Transaction):
        transaction.amount += self.balance

# ========= Zadanie 3 =============
@dataclass()
class Book:
    title: str
    author: str
    year: int
    price: float

    def apply_discount(self, discount: int):
        self.price = self.price - (self.price * discount)

# ========= Zadanie 4 =============
@dataclass()
class Product:
    name:str
    price:float = Field(..., ge=0.0)
    category:str = "General"


# ========= Zadanie 5 =============
class Car:
    brand:str
    model:str
    year:int

    def is_classic(self):
        return datetime.date.year - self.year > 25


# ========= Zadanie 6 =============
class ElectricVehicle:
    def fuel_type(self):
        return "electric"

class GasolineVehicle:
    def fuel_type(self):
        return "gasoline"

class HybridCar(ElectricVehicle, GasolineVehicle):
    def fuel_type(self):
        return "hybrid"


# ========= Zadanie 7 =============
class Person:
    def introduce(self):
        return "I am a person"

class Worker(Person):
    def introduce(self):
        return "I am a worker"

class Student(Person):
    def introduce(self):
        return "I am a student"

class WorkingStudent(Worker, Student):
    pass

print(WorkingStudent.mro())

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
        return False

# ========= Zadanie 9 =============
class FlyingVehicle:
    def move(self):
        return "I fly"

class WaterVehicle:
    def move(self):
        return "I sail"

class AmphibiousVehicle:
    def move(self):







