from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def get_type(self) -> str:
        pass

class WordDocument(Document):
    def get_type(self) -> str:
        return "Word file"

class PDFDocument(Document):
    def get_type(self) -> str:
        return "PDF file"

class ExcelDocument(Document):
    def get_type(self) -> str:
        return "Excel file"

class DocumentFactory:
    registeredExtensions = {}

    def RegisterExtension(self, extension:str, fileType:Document) -> None:
        self.registeredExtensions[extension] = fileType

    def createDocument(self, file_extension: str) -> Document:
        if file_extension in self.registeredExtensions:
            return self.registeredExtensions[file_extension]()

        raise ValueError

    # Zastosowanie statycznych instrukcji warunkowych
#     def createDocument(self, file_extension:str) -> Document:
#         if file_extension == ".docx":
#             return WordDocument()
#
#         if file_extension == ".pdf":
#             return PDFDocument()
#
#         raise ValueError
#
#
# factory = DocumentFactory()
# word = factory.createDocument(".docx")
# print(word.get_type())

factory = DocumentFactory()
factory.RegisterExtension(".docx", WordDocument)
factory.RegisterExtension(".pdf", PDFDocument)
factory.RegisterExtension(".xlsx", ExcelDocument)

word = factory.createDocument(".docx")
pdf = factory.createDocument(".pdf")
excel = factory.createDocument(".xlsx")

print(word.get_type())
print(pdf.get_type())
print(excel.get_type())