# ========= Zadanie 10 =============
class Robot:
    def operate(self) -> str:
        return "Performing task"

class AI:
    def think(self) -> str:
        return "Processing data"

class Android(Robot, AI):
    def self_learn(self) -> str:
        return "Self learning"

print(Robot().operate())
print(AI().think())
print(Android().operate())
print(Android().think())
print(Android().self_learn())