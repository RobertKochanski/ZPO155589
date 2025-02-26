# ========= Zadanie 19 =============
from abc import ABC, abstractmethod


class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass
    def execute_query(self) -> None:
        pass

class MySQLConnection(DatabaseConnection):
    def connect(self) -> str:
        return "Connect to MySQL logic"
    def execute_query(self) -> str:
        return "Execute query MySQL logic"

class PostgreSQLConnection(DatabaseConnection):
    def connect(self) -> str:
        return "Connect to PostgreSQL logic"
    def execute_query(self) -> str:
        return "Execute query PostgreSQL logic"

print(MySQLConnection().connect())
print(MySQLConnection().execute_query())
print(PostgreSQLConnection().connect())
print(PostgreSQLConnection().execute_query())