# ========= Zadanie 7 =============
class Person:
    def introduce(self):
        return "I am a person"

class Worker(Person):
    def introduce(self):
        return "I am a worker"

class Student(Person):
    def introduce(self):
        return "I am a student"

class WorkingStudent(Worker, Student):
    pass

print(WorkingStudent.mro())