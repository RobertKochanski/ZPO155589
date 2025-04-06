from typing import Self


class Iterator:
    n: int
    add: int
    limit: int
    vector: list

    def __init__(self, vector: list) -> None:
        self.n = len(vector)
        self.limit = 0
        self.add = -1
        self.vector = vector

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> int:
        if self.n > self.limit:
            self.n += self.add
            return self.vector[self.n]

        raise StopIteration


iterator = Iterator([4,5,3,2])

for i in iterator:
    print(i)


