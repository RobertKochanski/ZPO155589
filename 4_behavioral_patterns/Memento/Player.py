class PlayerState:
    position: list
    health: int
    equipment: list

    def __init__(self, position: list, health: int, equipment: list) -> None:
        self.position = position
        self.health = health
        self.equipment = equipment

class Memento:
    _states: list
    _i: int

    def __init__(self) -> None:
        self._states = []
        self._i: int = -1

    def save_state(self, state: PlayerState) -> None:
        if self._i != len(self._states) - 1:
            self._states = self._states[:self._i + 1]

        self._states.append(state)
        self._i += 1

    def undo(self) -> None:
        if self._i > 0:
            self._i -= 1

    def redo(self) -> None:
        if self._i < len(self._states) - 1:
            self._i += 1

    def read_state(self) -> PlayerState:
        return self._states[self._i]

class Player:
    position: list
    health: int
    equipment: list
    memento: Memento

    def __init__(self, position: list, health: int, equipment: list) -> None:
        self.position = position
        self.health = health
        self.equipment = equipment
        self.memento = Memento()
        self.save_state()

    def __str__(self):
        return f"Position: {self.position}, Health: {self.health}, Inventory: {self.equipment}"

    def move(self, new_position: list) -> None:
        self.position = new_position

    def damage(self, damage: int) -> None:
        self.health -= damage

    def heal(self, heal: int) -> None:
        self.health += heal

    def pickup_item(self, item: str) -> None:
        self.equipment.append(item)

    def save_state(self):
        state = PlayerState(self.position, self.health, self.equipment)
        self.memento.save_state(state)

    def undo(self):
        self.memento.undo()
        state = self.memento.read_state()
        self.position = state.position
        self.health = state.health
        self.equipment = state.equipment

    def redo(self):
        self.memento.redo()
        state = self.memento.read_state()
        self.position = state.position
        self.health = state.health
        self.equipment = state.equipment



player = Player([0,0,0], 100, [])
player.move([2, 1, 37])
print(player)
player.save_state()

player.pickup_item("training sword")
player.pickup_item("bucket (helmet)")
player.save_state()
print(f"After picked up training stuff: {player}")

player.damage(99)
player.save_state()
print(f"After badly injured: {player}")

player.undo()
print(f"Undo to previous save: {player}")

