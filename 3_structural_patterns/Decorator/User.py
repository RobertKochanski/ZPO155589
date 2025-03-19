from abc import ABC, abstractmethod
from typing import Any


class User:
    def __init__(self):
        self.roles = ["User"]

    def showRoles(self) -> list[str]:
        return self.roles.copy() # copy aby uniknąć modyfikacji klasy bazowej


class UserDecorator(ABC):
    def __init__(self, obj:Any) -> None:
        self.object = obj

    @abstractmethod
    def showRoles(self) -> Any:
        pass

class AdminDecorator(UserDecorator):
    def showRoles(self) -> list[str]:
        user_roles = self.object.showRoles()

        return user_roles + ["Admin"]

class ModeratorDecorator(UserDecorator):
    def showRoles(self) -> list[str]:
        user_roles = self.object.showRoles()

        return user_roles + ["Moderator"]

class GuestDecorator(UserDecorator):
    def showRoles(self) -> list[str]:
        user_roles = self.object.showRoles()

        return user_roles + ["Guest"]


user = User()
print(f"User1 after create: {user.showRoles()}")

user_admin = AdminDecorator(user)
print(f"User1 after AdminDecorator: {user_admin.showRoles()}")

user_moderator = ModeratorDecorator(user_admin)
print(f"User1 after AdminDecorator then ModeratorDecorator: {user_moderator.showRoles()}")

user2 = User()
user2_guest = GuestDecorator(user2)
print(f"User2 after create then GuestDeco: {user2_guest.showRoles()}")

user3 = User()
print(GuestDecorator(AdminDecorator(ModeratorDecorator(user3))).showRoles())
print(user3.showRoles())