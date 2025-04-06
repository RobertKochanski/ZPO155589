from typing import Self

class Order:
    name: str
    status: str

    def __init__(self, name: str, status: str):
        self.name = name
        self.status = status

class Iterator:
    orders: list[Order]
    status: str
    index: int

    def __init__(self, orders: list[Order], status: str):
        self.orders = orders
        self.status = status
        self.index = 0

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> Order:
        while self.index < len(self.orders):
            order = self.orders[self.index]
            self.index += 1
            if order.status == self.status:
                return order

        raise StopIteration


orders = [Order("1", "done"), Order("2", "undone"), Order("3", "done")]

iterator = Iterator(orders, "done")

for order in iterator:
    print(order.name, order.status)