class GraphicLib:
    @staticmethod
    def scale_image(image_path:str, width:int, height:int) -> dict:
        return {"image": image_path, "width": width, "height": height}

    @staticmethod
    def change_color(image_path:str, color:str):
        return {"image": image_path, "color": color}

    @staticmethod
    def compress_image(image_path:str, compress:str):
        return {"image": image_path, "compress": compress}


graphicLib = GraphicLib()
print(graphicLib.scale_image("Some image", 100, 200))
print(graphicLib.change_color("Some image", "#FFEEDD"))
print(graphicLib.compress_image("Some image", "compress"))