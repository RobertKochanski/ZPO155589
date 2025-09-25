from abc import ABC, abstractmethod

class Observable(ABC):
    _observers: set

    def __init__(self):
        self._observers = set()

    def add_observer(self, observer) -> None:
        self._observers.add(observer)

    def remove_observer(self, observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.notify(device=self)

class Observer(ABC):
    def __init__(self, observable: Observable) -> None:
        observable.add_observer(self)

    @abstractmethod
    def notify(self, *args: list, **kwargs: dict) -> None:
        pass

class Device(Observable):
    name: str

    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def sensor(self):
        self.notify()

    def __str__(self):
        return self.name

class TempNotify(Observer):
    temperature: float

    def notify(self, *args: list, **kwargs: dict) -> None:
        device = kwargs["device"]
        print(f"[Notify] {device}")


device = Device("temp")
tempNotify = TempNotify(device)

device.sensor()



