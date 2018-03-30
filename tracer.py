import numpy as np


class P3Image:
    def __init__(self, pixels):
        self.pixels = pixels
        width, height = pixels.shape

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
        pixel_str = ""
        for j in range(self.height-1, 0, -1):
            for i in range(self.width):
                pixel = [
                    int(255.99 * p) for p in [i / self.width, j / self.height, .2]
                ]

                r, g, b = pixel
                pixel_str += f"{r} {g} {b} "
            pixel_str += "\n"

        return pixel_str


if __name__ == "__main__":
    pixels = np.empty([200, 100])
    P3Image(pixels).write('test.ppm')
