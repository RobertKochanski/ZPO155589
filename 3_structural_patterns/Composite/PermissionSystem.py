from abc import ABC, abstractmethod


class Composite(ABC):
    @abstractmethod
    def add_permission(self, permission:str) -> None:
        pass

    @abstractmethod
    def get_permissions(self) -> None:
        pass

class User(Composite):
    name: str
    permissions: list[str]

    def __init__(self, name:str):
        self.name = name
        self.permissions = []

    def add_permission(self, permission:str) -> None:
        self.permissions.append(permission)

    def get_permissions(self) -> list[str]:
        return self.permissions


class UserGroup(Composite):
    name: str
    permissions: list[str]
    members: list[Composite]

    def __init__(self, name:str):
        self.name = name
        self.permissions = []
        self.members = []

    def add_permission(self, permission:str) -> None:
        self.permissions.append(permission)

    def get_permissions(self) -> set[str]:
        all_permissions = set(self.permissions)
        for member in self.members:
            all_permissions.update(member.get_permissions())  # Pobieramy uprawnienia z członków
        return all_permissions

    def add_member(self, member:Composite) -> None:
        self.members.append(member)


user1 = User("user1")
user2 = User("user2")

group1 = UserGroup("Group1")
group2 = UserGroup("Group2")

user1.add_permission("GET")
user1.add_permission("POST")
user1.add_permission("DELETE")
user2.add_permission("GET")

group1.add_permission("PUT")
group2.add_permission("PATCH")

group1.add_member(user1)
group1.add_member(group2)
group2.add_member(user2)

print(f"user1 - permissions {user1.get_permissions()}")
print(f"group1 - permissions {group1.permissions}")
print(f"group1 - all permissions for group {group1.get_permissions()}")