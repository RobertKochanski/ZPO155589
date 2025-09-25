from abc import ABC, abstractmethod

class Observable(ABC):
    _observers: set

    def __init__(self):
        self._observers = set()

    def add_observer(self, observer) -> None:
        self._observers.add(observer)

    def remove_observer(self, observer) -> None:
        self._observers.remove(observer)

    def turn_on(self, accident: bool) -> None:
        for observer in self._observers:
            observer.turn_on(accident)

class Observer(ABC):
    def __init__(self, observable: Observable) -> None:
        observable.add_observer(self)

    @abstractmethod
    def turn_on(self, accident: bool) -> None:
        pass

class Server(Observable):
    accident: bool

    def __init__(self) -> None:
        super().__init__()
        self.accident = False

    def accident_happened(self) -> None:
        self.accident = True
        self.turn_on(self.accident)

class Sms(Observer):
    power_on: bool = False

    def turn_on(self, accident: bool) -> None:
        if accident:
            self.power_on = True
            print("SMS system turned on")

class Email(Observer):
    power_on: bool = False

    def turn_on(self, accident: bool) -> None:
        if accident:
            self.power_on = True
            print("Email system turned on")

class Logs(Observer):
    power_on: bool = False

    def turn_on(self, accident: bool) -> None:
        if accident:
            self.power_on = True
            print("Logs system turned on")


server = Server()
smsSystem = Sms(server)
emailSystem = Email(server)
logSystem = Logs(server)

server.accident_happened()