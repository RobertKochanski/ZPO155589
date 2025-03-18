class FahrenheitSensor:
    number: float

    def __init__(self, number:float):
        self.number = number

    def degrees(self) -> float:
        return self.number

class Adapter:
    def __init__(self, fahrenheitSensor: FahrenheitSensor) -> None:
        self.fahrenheitSensor = fahrenheitSensor

    def toCelsius(self) -> float:
        #(fahrenheit - 32) * 5/9
        return (self.fahrenheitSensor.degrees() - 32) * 5/9


fahrenheitSensor = FahrenheitSensor(50.0)
print(f"{fahrenheitSensor.number} in Fahrenheit")

adapter = Adapter(fahrenheitSensor)
print(f"{adapter.toCelsius()} in Celsius")