import time
from abc import ABC, abstractmethod
import random

class AttackStrategy(ABC):
    @abstractmethod
    def attack(self, attacker, opponent) -> None:
        pass

class AggressiveAttack(AttackStrategy):
    def attack(self, attacker, opponent) -> None:
        print("Attacked Aggressively")
        if random.randint(1, 10) <= 5: # 50/50 chance
            print("You missed")
        else:
            opponent.health -= attacker.damage
            print(f"Your: {attacker.name} deals {attacker.damage} damage to {opponent.name}(hp:{opponent.health})")


class DefensiveAttack(AttackStrategy):
    def attack(self, attacker, opponent) -> None:
        opponent.health -= int(attacker.damage / 2)
        print("Attacked Defensively")
        print(f"Your: {attacker.name} deals {int(attacker.damage/2)} damage to {opponent.name}(hp:{opponent.health})")


class RandomAttack(AttackStrategy):
    def attack(self, attacker, opponent: "Character") -> None:
        print("Attacked Randomly")
        if random.randint(1, 10) <= 2: # 80/20 chance
            print("You missed")
        else:
            damage = random.randint(int(attacker.damage / 2), attacker.damage)
            opponent.health -= damage
            print(f"Your: {attacker.name} deals {damage} damage to {opponent.name}(hp:{opponent.health})")


class Character:
    name: str
    health: int
    damage: int
    strategy: AttackStrategy

    def __init__(self, name: str, health: int, damage: int, strategy: AttackStrategy) -> None:
        self.name = name
        self.health = health
        self.damage = damage
        self.strategy = strategy

    def attack(self, opponent: "Character") -> None:
        self.strategy.attack(self, opponent)

    def changeStrategy(self, newStrategy: AttackStrategy):
        self.strategy = newStrategy

    def introduce(self):
        print(f"Character {self.name}: \n   Health: {self.health}\n   Damage: {self.damage}")

    def battle(self, opponent: "Character") -> None:
        x = 1

        while self.health > 0 and opponent.health > 0:
            rand_strat = random.randint(1, 3)
            if rand_strat == 1:
                self.strategy = AggressiveAttack()
            if rand_strat == 2:
                self.strategy = DefensiveAttack()
            else:
                self.strategy = RandomAttack()

            opponent_strat = random.randint(1, 3)
            if opponent_strat == 1:
                opponent.strategy = AggressiveAttack()
            if opponent_strat == 2:
                opponent.strategy = DefensiveAttack()
            else:
                opponent.strategy = RandomAttack()

            print(f"Turn {x}")
            time.sleep(1)
            print(f"{self.name} attacks:")
            self.attack(opponent)
            if opponent.health <= 0:
                print(f"{self.name} win")
                return
            time.sleep(1)
            print(f"{opponent.name} attacks:")
            opponent.attack(char1)
            if self.health <= 0:
                print(f"{opponent.name} win")
                return
            time.sleep(1)
            x += 1


char1 = Character("Warrior", 100, 10, AggressiveAttack())
char2 = Character("Mage", 80, 15, RandomAttack())

char1.battle(char2)
