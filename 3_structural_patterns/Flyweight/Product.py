class ProductShared:
    name:str
    barcode:str

    def __init__(self, name:str, barcode:str):
        self.name = name
        self.barcode = barcode

    def sharedInfo(self):
        print(f"Product: {self.name} with barcode: {self.barcode}")


class ProductSharedFactory:
    part: dict[str, ProductShared] = {}

    def get_part_prod(self, name: str, barcode: str) -> ProductShared:
        key = f"{name}-{barcode}"
        if key not in self.part:
            self.part[key] = ProductShared(name, barcode)
        return self.part[key]


class Product:
    location:str
    stock:str

    def __init__(self, prodShared:ProductShared, location:str, stock:str):
        self.prodShared = prodShared
        self.location = location
        self.stock = stock

    def info(self):
        self.prodShared.sharedInfo()
        print(f"Location: {self.location}")
        print(f"Stock: {self.stock}")


factory = ProductSharedFactory()

milk_part = factory.get_part_prod("Milk", "123456")
milk2_part = factory.get_part_prod("Milk", "123456")
kremowka_part = factory.get_part_prod("Kremówka", "2137")

milk = Product(milk_part, "Olsztyn", "10")
milk2 = Product(milk2_part, "Warszawa", "8")
kremowka = Product(kremowka_part, "Watykan", "100")

print(f"Check if milk_part is milk2_part (same name and barcode): {milk_part is milk2_part}")

kremowka_part.sharedInfo()

kremowka.info()