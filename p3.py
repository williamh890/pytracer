
class P3Image:
    def __init__(self, pixels):
        self.pixels = pixels
        width, height, channels = pixels.shape
        assert(channels == 3)

        self.width = width
        self.height = height

        self.type = "P3"
        self.max_color = 255

    def write(self, file_name):
        img_str = self.get()

        with open(file_name, "w") as f:
            f.write(img_str)

    def get(self):
        return \
            f"""{self.type}
{self.width} {self.height}
{self.max_color}
{self.get_formatted_pixels()}"""

    def get_formatted_pixels(self):
        self.pixels *= 255
        pixels = self.pixels.astype('uint8')
        pixel_str = ""
        for j in range(self.height-1, 0, -1):
            for i in range(self.width):
                r, g, b = pixels[i][j]
                pixel_str += f"{r} {g} {b} "
            pixel_str += "\n"

        return pixel_str
