from typing import Generator

def harmonic_generator(stop: int) -> Generator:
    yield 1     # prevent to print 1/1

    denominator = 2
    while denominator < stop:
        yield f"1/{denominator} - {round(1/denominator, 3)}"
        denominator += 1


gen = harmonic_generator(10)

for i in gen:
    print(i)