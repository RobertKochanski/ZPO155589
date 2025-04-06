from abc import ABC, abstractmethod

class Document(ABC):
    name:str
    extension:str

    def __init__(self, name:str, extension:str):
        self.name = name
        self.extension = extension

    @abstractmethod
    def write_file(self) -> None:
        pass

    @abstractmethod
    def read_file(self) -> None:
        pass

    @abstractmethod
    def delete_file(self) -> None:
        pass

    def processing_file(self):
        print(f"Processing file {self.name}{self.extension}...")
        self.write_file()
        self.read_file()
        self.delete_file()

class PDF(Document):
    def write_file(self) -> None:
        print("Writing PDF file")

    def read_file(self) -> None:
        print("Reading PDF file")

    def delete_file(self) -> None:
        print("Deleting PDF file")


class DOCX(Document):
    def write_file(self) -> None:
        print("Writing DOCX file")

    def read_file(self) -> None:
        print("Reading DOCX file")

    def delete_file(self) -> None:
        print("Deleting DOCX file")


class TXT(Document):
    def write_file(self) -> None:
        print("Writing TXT file")

    def read_file(self) -> None:
        print("Reading TXT file")

    def delete_file(self) -> None:
        print("Deleting TXT file")


pdf = PDF("pdf_file", ".pdf")
doc = DOCX("document", ".docx")
txt = TXT("text", ".txt")

pdf.processing_file()