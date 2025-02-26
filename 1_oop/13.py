# ========= Zadanie 13 =============
class Store:
    total_customers: int = 5

    @classmethod
    def add_customer(cls) -> None:
        cls.total_customers += 1

    @classmethod
    def get_total_customers(cls) -> int:
        return cls.total_customers

print(Store.get_total_customers())
Store.add_customer()
print(Store.get_total_customers())