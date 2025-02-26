# ========= Zadanie 1 =============
class Employee:
    first_name: str
    last_name: str
    salary: float

    def __init__(self, first_name:str, last_name:str, salary:float):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self) -> str:
        return f"{self.first_name + ' ' + self.last_name}"


class Manager(Employee):
    department: str

    def __init__(self, first_name:str, last_name:str, salary:float, department:str):
        super().__init__(first_name, last_name, salary)
        self.department = department

    def get_department_info(self) -> str:
        return self.department

employee = Employee("Jan", "Kowalski", 5000)
print(employee.get_full_name())

manager = Manager("Andrzej", "Nowak", 10000, "department")
print(manager.get_full_name())
print(manager.get_department_info())
