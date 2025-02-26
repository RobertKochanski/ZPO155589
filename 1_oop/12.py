# ========= Zadanie 12 =============
class IDGenerator:
    id: int = 0

    @classmethod
    def generate_id(cls) -> int:
        cls.id += 1
        return cls.id

print(IDGenerator.generate_id()) # 1
print(IDGenerator.generate_id()) # 2
print(IDGenerator.generate_id()) # 3