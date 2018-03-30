from ray import Ray
from p3 import P3Image
from utils import normalized, vec3, pixel

import numpy as np


def get_example_pixels_np():
    pixels = np.empty([200, 100, 3], dtype="float")
    width, height, channels = pixels.shape

    lower_left_corner = vec3(-2., -1., -1.)
    horizontal = vec3(4., 0., 0.)
    vertical = vec3(0., 2., 0.)
    origin = vec3(0., 0., 0.)

    for y in range(height):
        for x in range(width):
            u, v = x / 200, y / 100
            direction = lower_left_corner + u*horizontal + v*vertical
            color = Ray(origin, direction).color
            pixels[x][y] = color

    return pixels


if __name__ == "__main__":
    pixels = get_example_pixels_np()

    P3Image(pixels).write('test.ppm')
