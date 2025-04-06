from abc import ABC, abstractmethod

class Generator(ABC):
    def get_data(self) -> None:
        print("Get basic data...")

    @abstractmethod
    def prepare_data(self) -> None:
        pass

    @abstractmethod
    def generate_file(self) -> None:
        pass

    def send_file(self) -> None:
        print("Sending generated file...")

    def generateReport(self):
        self.get_data()
        self.prepare_data()
        self.generate_file()
        self.send_file()

class CsvGenerator(Generator):
    def prepare_data(self) -> None:
        print("Preparing data...")

    def generate_file(self) -> None:
        print("Generating CSV file...")

class JsonGenerator(Generator):
    def get_data(self) -> None:
        print("Getting Json data...")

    def prepare_data(self) -> None:
        print("Preparing data...")

    def generate_file(self) -> None:
        print("Generating JSON file...")

class XMLGenerator(Generator):
    def prepare_data(self) -> None:
        print("Preparing data...")

    def generate_file(self) -> None:
        print("Generating XML file...")


json = JsonGenerator()
json.generateReport()

xml = XMLGenerator()
xml.generateReport()