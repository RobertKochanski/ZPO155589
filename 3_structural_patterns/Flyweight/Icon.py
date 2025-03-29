class Icon:
    image:str

    def __init__(self, image:str):
        self.image = image

    def display(self):
        print(self.image)

class IconFactory:
    def __init__(self):
        self.icons = {}

    def get_icon(self, image):
        if image not in self.icons:
            self.icons[image] = Icon(image)
        return self.icons[image]

factory = IconFactory()

icon1 = factory.get_icon("icon1")
icon2 = factory.get_icon("icon2")

icon1.display()
icon2.display()
