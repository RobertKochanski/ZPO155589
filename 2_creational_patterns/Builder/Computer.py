class Computer:
    CPU: str
    GPU: str
    RAM: int
    OS: str
    HardDrive: str
    PowerSupply: int
    Case: str

    # def __init__(self, CPU:str, GPU:str, RAM:int, OS:str, HardDrive:str, PowerSupply:int, Case:str):
    #     self.CPU = CPU
    #     self.GPU = GPU
    #     self.RAM = RAM
    #     self.OS = OS
    #     self.HardDrive = HardDrive
    #     self.PowerSupply = PowerSupply
    #     self.Case = Case

class ComputerBuilder:

    def __init__(self):
        self.computer = Computer()

    def setCPU(self, cpu:str) -> object:
        self.computer.CPU = cpu
        return self

    def setGPU(self, gpu:str) -> object:
        self.computer.GPU = gpu
        return self

    def setRAM(self, ram:int) -> object:
        self.computer.RAM = ram
        return self

    def setOS(self, os:str) -> object:
        self.computer.OS = os
        return self

    def setHardDrives(self, hardDrives:str) -> object:
        self.computer.HardDrive = hardDrives
        return self

    def setPowerSupply(self, powerSupply:int) -> object:
        self.computer.PowerSupply = powerSupply
        return self

    def setCase(self, case:str) -> object:
        self.computer.Case = case
        return self

    def build(self) -> Computer:
        return self.computer


computer = ComputerBuilder().setCPU("added CPU").setGPU("added GPU").setRAM(5).build()

print(computer.CPU)
print(computer.GPU)
print(f"{computer.RAM} GB")