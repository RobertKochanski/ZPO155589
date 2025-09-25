from abc import ABC, abstractmethod

class Observable(ABC):
    _observers: set

    def __init__(self):
        self._observers = set()

    def add_observer(self, observer) -> None:
        self._observers.add(observer)

    def remove_observer(self, observer) -> None:
        self._observers.remove(observer)

    def notify(self, ratio: float, new_ratio: float) -> None:
        for observer in self._observers:
            observer.notify(self, ratio, new_ratio)

class Observer(ABC):
    def __init__(self, observable: Observable) -> None:
        observable.add_observer(self)

    @abstractmethod
    def notify(self, observable, ratio, new_ratio) -> None:
        pass

class PLN_Dollar(Observable):
    ratio: float
    name: str

    def __init__(self, ratio: float):
        super().__init__()
        self.ratio = ratio
        self.name = f"PLN -> Dollar"

    def change_ratio(self, new_ratio: float) -> None:
        self.notify(self.ratio, new_ratio)
        self.ratio = new_ratio


class User(Observer):
    def notify(self, observable, ratio: float, new_ratio: float) -> None:
        if new_ratio != ratio:
            print(f"[User notified] {observable.name}. Ratio changed from {ratio} to {new_ratio}")


pln_dollar = PLN_Dollar(4.20)
user1 = User(pln_dollar)
user2 = User(pln_dollar)

pln_dollar.change_ratio(4.21)

