from abc import ABC, abstractmethod

class Device(ABC):
    power_on:bool

    def __init__(self):
        self.power_on = False

    @abstractmethod
    def powerOn(self):
        pass

    @abstractmethod
    def powerOff(self):
        pass

    @abstractmethod
    def setVolume(self, volume:int):
        pass

    @abstractmethod
    def get_status(self):
        pass


class TV(Device):
    volume:int
    channel:int

    def __init__(self, volume:int, channel:int):
        super().__init__()
        self.volume = volume
        self.channel = channel

    def powerOn(self):
        self.power_on = True

    def powerOff(self):
        self.power_on = False

    def setVolume(self, volume:int):
        self.volume = volume

    def get_status(self) -> str:
        return f"TV | Power: {self.power_on}, Volume: {self.volume}, Channel: {self.channel}"


class Radio(Device):
    volume:int
    frequency:float

    def __init__(self, volume:int):
        super().__init__()
        self.volume = volume
        self.frequency = 95.3

    def powerOn(self):
        self.power_on = True

    def powerOff(self):
        self.power_on = False

    def setVolume(self, volume:int):
        self.volume = volume

    def get_status(self) -> str:
        return f"Radio | Power: {self.power_on}, Volume: {self.volume}, {self.frequency}-RMF FM Olsztyn"

class Drone(Device):
    height:float

    def __init__(self, height:float):
        super().__init__()
        self.height = height

    def powerOn(self):
        self.power_on = True

    def powerOff(self):
        self.power_on = False

    def checkHeight(self, height:float):
        self.height = height

    def setVolume(self, volume:int):
        pass

    def get_status(self) -> str:
        return f"Drone | Power: {self.power_on}, Height: {self.height}m"

class RemoteControl:
    device: Device

    def __init__(self, device: Device):
        self.device = device

    def powerOn(self):
        self.device.powerOn()

    def powerOff(self):
        self.device.powerOff()

    def setVolume(self, volume:int):
        self.device.setVolume(volume)

    def checkHeight(self, height:float):
        self.device.checkHeight(height)

    def get_status(self):
        return self.device.get_status()




tv = TV(25, 1)
controller = RemoteControl(tv)
print(controller.get_status())

radio = Radio(100)
controller = RemoteControl(radio)
print(controller.get_status())