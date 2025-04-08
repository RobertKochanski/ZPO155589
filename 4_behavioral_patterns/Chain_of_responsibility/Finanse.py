from abc import ABC, abstractmethod
from typing import Optional


class Approve(ABC):
    name: str
    next_approve: Optional["Approve"]

    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def approve_request(self, request: float) -> None:
        pass

    def set_next_approve(self, next_approve: "Approve") -> None:
        self.next_approve = next_approve

class Manager(Approve):
    def approve_request(self, request: float) -> None:
        if request < 100:
            print(f"{self.name}: APPROVED")
        elif self.next_approve:
            self.next_approve.approve_request(request)

class COO(Approve):
    def approve_request(self, request: float) -> None:
        if request < 500:
            print(f"{self.name}: APPROVED")
        elif self.next_approve:
            self.next_approve.approve_request(request)

class CTO(Approve):
    def approve_request(self, request: float) -> None:
        if request < 1000:
            print(f"{self.name}: APPROVED")
        elif self.next_approve:
            self.next_approve.approve_request(request)

class CEO(Approve):
    def approve_request(self, request: float) -> None:
        if request < 5000:
            print(f"{self.name}: APPROVED")
        else:
            print(f"{self.name}: NOT APPROVED")


ceo = CEO("CEO")

cto = CTO("CTO")
cto.set_next_approve(ceo)

coo = COO("COO")
coo.set_next_approve(cto)

manager = Manager("Manager")
manager.set_next_approve(coo)

manager.approve_request(400)