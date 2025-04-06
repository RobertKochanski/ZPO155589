from abc import ABC, abstractmethod


class SortStrategy(ABC):
    @abstractmethod
    def sort(self, vector: list) -> None:
        pass

class QuickSort(SortStrategy):
    def sort(self, vector: list) -> None:
        print("Sorted with Quick Sort")

class BubbleSort(SortStrategy):
    def sort(self, vector: list) -> None:
        print("Sorted with Bubble Sort")

class Sort:
    strategy: SortStrategy

    def sort_(self, vector: list) -> None:
        if len(vector) > 10:
            self.strategy = QuickSort()
            self.strategy.sort(vector)
        else:
            self.strategy = BubbleSort()
            self.strategy.sort(vector)


x: list[int] = [1, 4, 3, 6]
y: list[int] = [0,1,2,3,4,5,6,7,8,9,10]

sort_ = Sort()
sort_.sort_(x)
sort_.sort_(y)

