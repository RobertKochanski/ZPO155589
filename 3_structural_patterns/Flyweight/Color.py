class Color:
    red:int
    green:int
    blue:int

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def get_color(self):
        print(f"Color: {self.red, self.green, self.blue}")


class ColorFactory:
    colors: dict[str, Color] = {}

    def get_color(self, rgb: tuple) -> Color:
        key = f"{rgb}"
        if key not in self.colors:
            self.colors[key] = Color(rgb[0], rgb[1], rgb[2])
        return self.colors[key]


class Shape:
    def __init__(self, shape: str, color: Color, size: int):
        self.shape = shape
        self.color = color
        self.size = size

    def info(self):
        print(f"{self.shape} with size: {self.size} and color: R {self.color.red}, G {self.color.green}, B {self.color.blue}")


factory = ColorFactory()

azure_tuple = (0, 127, 255)
azure = factory.get_color(azure_tuple)

azure_again = factory.get_color(azure_tuple)

print(azure is azure_again)

eggshell_tuple = (228, 227, 211)
eggshell = factory.get_color(eggshell_tuple)


circle = Shape("circle", azure, 100)
square = Shape("square", eggshell, 200)

circle.info()
square.info()