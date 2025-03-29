from abc import ABC, abstractmethod


class ShapeRenderer(ABC):
    @abstractmethod
    def render_circle(self, radius:float) -> None:
        pass

    @abstractmethod
    def render_rectangle(self, w:float, h:float) -> None:
        pass

class SVGRenderer(ShapeRenderer):
    def render_circle(self, radius:float) -> None:
        print(f"SVG renderer circle with radius {radius}")

    def render_rectangle(self, w:float, h:float) -> None:
        print(f"SVG renderer rectangle with w {w} h {h}")

class BMPRenderer(ShapeRenderer):
    def render_circle(self, radius:float) -> None:
        print(f"BMP renderer circle with radius={radius}")

    def render_rectangle(self, w:float, h:float) -> None:
        print(f"BMP renderer rectangle with w={w} and h={h}")


class Shape(ABC):
    renderer: ShapeRenderer

    def __init__(self, renderer:ShapeRenderer):
        self.renderer = renderer

    @abstractmethod
    def drawShape(self) -> None:
        pass

class Circle(Shape):
    radius:float

    def __init__(self, radius: float, renderer: ShapeRenderer):
        super().__init__(renderer)
        self.radius = radius

    def drawShape(self) -> None:
        self.renderer.render_circle(self.radius)

class Rectangle(Shape):
    w:float
    h:float

    def __init__(self, w: float, h: float, renderer: ShapeRenderer):
        super().__init__(renderer)
        self.w = w
        self.h = h

    def drawShape(self) -> None:
        self.renderer.render_rectangle(self.w, self.h)


svg = SVGRenderer()
bmp = BMPRenderer()

circle = Circle(8, svg)
rectangle = Rectangle(10, 5, bmp)

circle.drawShape()
rectangle.drawShape()