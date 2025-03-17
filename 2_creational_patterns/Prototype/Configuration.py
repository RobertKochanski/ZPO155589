from copy import deepcopy
from dataclasses import dataclass
from typing import Any


@dataclass
class Configuration:
    dark_mode: bool
    font_size: int
    conf1: str
    conf2: str


class Prototype:
    def __init__(self) -> None:
        self.objects = dict()

    def add_prototype(self, id_: int, obj: Any) -> None:
        self.objects[id_] = obj

    def del_prototype(self, id_: int) -> None:
        del self.objects[id_]

    def clone(self, id_: int, **kwargs: dict) -> Any:
        if id_ in self.objects:
            instance = deepcopy(self.objects[id_])

            for key in kwargs:
                setattr(instance, key, kwargs[key])

            return instance
        else:
            raise ModuleNotFoundError("ID not found!")


prototype = Prototype()

configuration = Configuration(True, 16, "conf1", "conf2")

prototype.add_prototype(1 ,configuration)

conf2 = prototype.clone(1, dark_mode=False, conf1="conf11")

print(configuration)
print(conf2)
