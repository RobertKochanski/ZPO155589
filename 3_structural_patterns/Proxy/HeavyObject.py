class HeavyObject:
    def pickUp(self) -> None:
        print("Heavy Ho")

class HeavyObjectProxy:
    heavyObject: HeavyObject

    def __init__(self):
        self.heavyObject = None

    def _createHeavyObject(self):
        if self.heavyObject is None:
            self.heavyObject = HeavyObject()

    def pickUp(self):
        self._createHeavyObject()
        self.heavyObject.pickUp()


heavyObjectProxy = HeavyObjectProxy()
print(f"Object before use: {heavyObjectProxy.heavyObject}")

heavyObjectProxy.pickUp()
print(f"Object after use: {heavyObjectProxy.heavyObject}")
