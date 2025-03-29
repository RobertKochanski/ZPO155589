class File:
    name: str
    extension: str

    def __init__(self, name: str, extension: str):
        self.name = name
        self.extension = extension

    def read(self):
        print(f"Read file: {self.name}.{self.extension}")

class FileProxy:
    user: str
    usersPermitted: set[str]
    file: File

    def __init__(self, user: str, usersPermitted:set[str], file: File):
        self.user = user
        self.usersPermitted = usersPermitted
        self.file = file

    def read(self):
        if self.user in self.usersPermitted:
            self.file.read()
        else:
            print(f"{self.user} not permitted")


file = File("name", "txt")
fileProxy = FileProxy("user", ["user", "admin"], file)
fileProxy.read()

fileProxy2 = FileProxy("user", ["admin"], file)
fileProxy2.read()