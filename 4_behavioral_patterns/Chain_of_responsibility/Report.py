from abc import ABC, abstractmethod
from typing import Optional

class Report:
    type: str
    description: str

    def __init__(self, type: str, description: str):
        self.type = type
        self.description = description

class ReportHandler(ABC):
    next_handler: Optional["ReportHandler"]

    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, handler: "ReportHandler"):
        self.next_handler = handler
        return handler

    @abstractmethod
    def handle(self, report: Report) -> None:
        pass

class TechnicalReportHandler(ReportHandler):
    def handle(self, report: Report) -> None:
        if report.type.lower() == "technical":
            self.technical_report()
        elif self.next_handler:
            self.next_handler.handle(report)
        else:
            print("No handler found")

    @staticmethod
    def technical_report():
        print("Technical Report")


class ITReportHandler(ReportHandler):
    def handle(self, report: Report) -> None:
        if report.type.upper() == "IT":
            self.IT_report()
        elif self.next_handler:
            self.next_handler.handle(report)
        else:
            print("No handler found")

    @staticmethod
    def IT_report():
        print("IT Report")


report = Report("hehe", "website dont work, please help")

handler = TechnicalReportHandler()
handler.set_next_handler(ITReportHandler())

handler.handle(report)