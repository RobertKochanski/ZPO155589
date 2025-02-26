# ========= Zadanie 14 =============
class MathOperations:
    @staticmethod
    def add(a:float, b:float) -> float:
        return a + b

    @staticmethod
    def multiply(a:float, b:float) -> float:
        return a * b

    @classmethod
    def identity_matrix(cls, size:int):
        return [[0]*size for i in range(size)]

print(MathOperations.add(2, 3))
print(MathOperations.multiply(2, 3))
print(MathOperations.identity_matrix(3))