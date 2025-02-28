class Computer:
    CPU: str
    GPU: str
    RAM: int
    OS: str
    HardDrive: str
    PowerSupply: int
    Case: str

    def __init__(self, CPU:str, GPU:str, RAM:int, OS:str, HardDrive:str, PowerSupply:int, Case:str):
        self.CPU = CPU
        self.GPU = GPU
        self.RAM = RAM
        self.OS = OS
        self.HardDrive = HardDrive
        self.PowerSupply = PowerSupply
        self.Case = Case
