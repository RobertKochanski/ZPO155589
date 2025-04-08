from abc import ABC, abstractmethod
from typing import Optional


class Email:
    from_: str
    to: str
    subject: str
    body: str
    has_virus: bool

    def __init__(self, from_: str, to: str, subject: str, body: str, has_virus: bool):
        self.from_ = from_
        self.to = to
        self.subject = subject
        self.body = body
        self.has_virus = has_virus

class EmailChecker(ABC):
    next_check: Optional["EmailChecker"]

    def __init__(self):
        self.next_check = None

    def handle(self, email: Email) -> str:
        if self.check(email):
            if self.next_check:
                return self.next_check.handle(email)
            else:
                return "Email clear"
        else:
            return f"Email blocked by: {self.__class__.__name__}"

    def set_next_check(self, next_check: "EmailChecker") -> "EmailChecker":
        self.next_check = next_check
        return next_check

    @abstractmethod
    def check(self, email: "Email") -> None:
        pass

class HeaderCheck(EmailChecker):
    def check(self, email: Email) -> bool:
        print("Header check...")
        if "header" in email.subject:
            return False
        return True

class SpamCheck(EmailChecker):
    def check(self, email: Email) -> bool:
        print("Spam check...")
        if "spam" in email.body:
            return False
        return True

class VirusCheck(EmailChecker):
    def check(self, email: Email) -> bool:
        print("Virus check...")
        if email.has_virus:
            return False
        return True

class OtherCheck(EmailChecker):
    def check(self, email: Email) -> bool:
        print("Other problems check...")
        if "Any problem" in email.body:
            return False
        return True


checker_chain = HeaderCheck()
checker_chain.set_next_check(SpamCheck()).set_next_check(VirusCheck()).set_next_check(OtherCheck())

email1 = Email("from", "to", "subject", "body", False)

print(checker_chain.handle(email1))

