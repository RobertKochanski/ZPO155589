from abc import ABC, abstractmethod

class Renderer(ABC):
    @abstractmethod
    def render(self, document: "Document") -> None:
        pass

class LightThemeRenderer(Renderer):
    def render(self, document: "Document") -> None:
        print(f"{document.name}{document.extension} opened with light mode")

class DarkThemeRenderer(Renderer):
    def render(self, document: "Document") -> None:
        print(f"{document.name}{document.extension} opened with dark mode")

class Document(ABC):
    def __init__(self, name: str, content: str, renderer: Renderer):
        self.name = name
        self.extension = ".pdf"
        self.content = content
        self.renderer = renderer

    @abstractmethod
    def show(self) -> None:
        pass

class PDFDocument(Document):
    def show(self) -> None:
        self.renderer.render(self)


light_renderer = LightThemeRenderer()
dark_renderer = DarkThemeRenderer()

light_doc = PDFDocument("white", "some white content", light_renderer)
dark_doc = PDFDocument("black", "some black content", dark_renderer)

light_doc.show()
dark_doc.show()
