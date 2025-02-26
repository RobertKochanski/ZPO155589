# ========= Zadanie 15 =============
class GameCharacter:
    default_health:int = 100
    health = default_health

    def restore_health(self):
        self.health = GameCharacter.default_health

    @classmethod
    def set_default_health(cls, value):
        cls.default_health = value

print(f"Default HP: {GameCharacter.default_health}")
character1 = GameCharacter()
character2 = GameCharacter()
print(f"Character 1: {character1.health}")
print(f"Character 2: {character2.health}")
GameCharacter.set_default_health(150)
print(f"Default HP (after change): {GameCharacter.default_health}")
character1.restore_health()
print(f"Character 1 (restored): {character1.health}")
print(f"Character 2: {character2.health}")