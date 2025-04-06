from abc import ABC, abstractmethod

class Tax(ABC):
    @abstractmethod
    def tax_calculate(self, value: float) -> float:
        pass

class PolandTax(Tax):
    def tax_calculate(self, value: float) -> float:
        return round(value * 0.23, 2) # 23% złodzieje


class SwitzerlandTax(Tax):
    def tax_calculate(self, value: float) -> float:
        return round(value * 0.081, 2) # 8,1%


class TaxCalculator:
    strategy: Tax

    def __init__(self, strategy: Tax):
        self.strategy = strategy

    def change_strategy(self, strategy: Tax) -> None:
        self.strategy = strategy

    def calculate_tax(self, value: float) -> float:
        return self.strategy.tax_calculate(value)


value = 123

calculator = TaxCalculator(PolandTax())
print(calculator.calculate_tax(value))

calculator.change_strategy(SwitzerlandTax())
print(calculator.calculate_tax(value))

