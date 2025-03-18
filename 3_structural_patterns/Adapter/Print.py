class PrintOld:
    def print_old(self) -> str:
        return "Some old print"

class Adapter:
    def __init__(self, printOld:PrintOld) -> None:
        self.printOld = printOld

    def print_new(self) -> str:
        return self.printOld.print_old() + " but in new one print"


printOld = PrintOld()
print(printOld.print_old())

adapter = Adapter(printOld)
print(adapter.print_new())