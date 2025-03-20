class RabbitMQ:
    def query(self) -> None:
        print("Query with RabbitMQ")

    def introduce(self) -> None:
        print("I'm RabbitMQ system")

class Kafka:
    def query(self) -> None:
        print("Query with Kafka")

    def introduce(self) -> None:
        print("I'm Kafka system")


class Facade:
    rabbitMQ: RabbitMQ
    kafka: Kafka

    def __init__(self):
        self.rabbitMQ = RabbitMQ()
        self.kafka = Kafka()

    def choose_system(self, name:str):
        if name == "Kafka":
            return self.kafka
        elif name == "RabbitMQ":
            return self.rabbitMQ
        else:
            return


facade = Facade()

kafka = facade.choose_system("Kafka")

kafka.introduce()