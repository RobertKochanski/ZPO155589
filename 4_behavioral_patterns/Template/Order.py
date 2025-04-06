from abc import ABC, abstractmethod

class Order(ABC):

    @abstractmethod
    def package(self) -> None:
        pass

    @abstractmethod
    def payment(self) -> None:
        pass

    @abstractmethod
    def deliver(self) -> None:
        pass

    def process_order(self):
        self.payment()
        self.package()
        self.deliver()


class StandardOrder(Order):
    def package(self) -> None:
        print("Standard Order - package")

    def payment(self) -> None:
        print("Standard Order - payment")

    def deliver(self) -> None:
        print("Standard Order - deliver within 5 work day")

class ExpressOrder(Order):
    def package(self) -> None:
        print("Express Order - package")

    def payment(self) -> None:
        print("Express Order - payment")

    def deliver(self) -> None:
        print("Express Order - deliver within 2 work day")

class PersonalPickup(Order):
    def package(self) -> None:
        print("Personal Pickup Order - package")

    def payment(self) -> None:
        print("Personal Pickup Order - payment")

    def deliver(self) -> None:
        print("Personal Pickup Order - pick up at the store")


personal = PersonalPickup()
personal.process_order()

express = ExpressOrder()
express.process_order()