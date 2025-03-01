# ========= Zadanie 14 =============
class MathOperations:
    @staticmethod
    def add(a:float, b:float) -> float:
        return a + b

    @staticmethod
    def multiply(a:float, b:float) -> float:
        return a * b

    @classmethod
    def identity_matrix(cls, size:int) -> []:
        matrix = [[0]*size for i in range(size)]
        for j in range(size):
            matrix[j][j] = 1
        return matrix

print(MathOperations.add(2, 3))
print(MathOperations.multiply(2, 3))
print(MathOperations.identity_matrix(3))