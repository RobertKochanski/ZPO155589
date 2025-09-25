from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def turn_on(self) -> None:
        pass

    @abstractmethod
    def turn_off(self) -> None:
        pass

class Light(Device):
    def turn_on(self) -> None:
        print("light on")

    def turn_off(self) -> None:
        print("light off")

class Heating(Device):
    def turn_on(self) -> None:
        print("heating on")

    def turn_off(self) -> None:
        print("heating off")

class Command(ABC):
    device: Device

    def __init__(self, device: Device):
        self.device = device

    @abstractmethod
    def execute(self) -> None:
        pass

class DeviceOn(Command):
    def execute(self) -> None:
        self.device.turn_on()

class DeviceOff(Command):
    def execute(self) -> None:
        self.device.turn_off()

class RemoteController:
    history: list

    def __init__(self):
        self.history = []

    def execute(self, command) -> None:
        self.history.append(command)
        command.execute()

    def show_history(self) -> None:
        x = 0
        print("History:")
        for command in self.history:
            x = x + 1
            print(f"{x}. Command: {command.__class__.__name__}, on {command.device.__class__.__name__} device")



light = Light()
heating = Heating()

control = RemoteController()

control.execute(DeviceOn(light))
control.execute(DeviceOn(heating))
control.execute(DeviceOff(light))

control.show_history()