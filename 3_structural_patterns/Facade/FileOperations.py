import os


class File:
    @staticmethod
    def write_file(filename:str, content: str) -> None:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"File {filename} saved")

    @staticmethod
    def read_file(filename:str) -> str:
        if not os.path.exists(filename):
            print(f"Cannot find file {filename}")
            return
        with open(filename, 'r') as file:
            content = file.read()
        return content

    @staticmethod
    def delete_file(filename:str) -> None:
        if not os.path.exists(filename):
            print(f"Cannot find file {filename}")
        else:
            os.remove(filename)
            print(f"File {filename} deleted")


file = File()
fileName = "FileFacade"

file.write_file(fileName, "Test for file operations facade")

content = file.read_file(fileName)
print(content)

file.delete_file(fileName)