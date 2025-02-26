# ========= Zadanie 4 =============
from dataclasses import dataclass, field


@dataclass()
class Product:
    name:str
    price:float
    category:str = field(default="General")

    # Check value after __init__
    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price >= 0")

# work properly
product = Product("name2", 10)
print(product)

# throw ValueError
product2 = Product("name", -1)


