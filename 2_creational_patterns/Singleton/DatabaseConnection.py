from typing import Self

class DatabaseConnection:
    _instance = None
    _configured:bool = False

    def __new__(cls, host="localhost", port=2137, user="admin", password="admin") -> Self:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._host = host
            cls._instance._port = port
            cls._instance._user = user
            cls._instance._password = password
            cls._configured = True
        return cls._instance

    def get_config(self) -> dict:
        return {
            "host": self._host,
            "port": self._port,
            "user": self._user,
            "password": self._password
        }

    def set_config(self, host, port, user, password) -> None | Exception:
        if self._configured:
            raise Exception("The configuration has already been set and cannot be changed.")
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self._configured = True


db1 = DatabaseConnection(host="127.0.0.1")
db2 = DatabaseConnection()
print(db1.get_config())
print(db2.get_config())

# try-catch dla przyjemniejszego dla oka wyjątku
try:
    db1.set_config(host="local", port=1410, user="root", password="secret")
except Exception as e:
    print(e)

# Hermetyzacja powinna zablokować te odwołanie do _host ale jest ona tylko umowna,
# więc ten kod nie powinien istnieć
# db1._instance._host = "ehh Python"
# print(db1.get_config())


