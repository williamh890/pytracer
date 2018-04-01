from ray import Ray
from p3 import P3Image
from utils import normalized, vec3, pixel, Range
from sphere import Sphere
from hitable_list import HitableList

import numpy as np
import sys

WIDTH, HEIGHT = 200, 100
INFINITY = sys.float_info.max


def color(ray, world):
    t_range = Range(0., INFINITY)
    hit = world.does_hit(ray, t_range)

    if hit is not None:
        return .5 * (hit.normal + 1.)

    unit_dir = normalized(ray.direction)
    t = .5 * (unit_dir[1] + 1.)

    return (1. - t) * vec3(1., 1., 1.) + \
        t * vec3(.5, .7, 1.)


def get_example_pixels_np():
    pixels = np.empty([WIDTH, HEIGHT, 3], dtype="float")
    width, height, channels = pixels.shape

    lower_left_corner = vec3(-2., -1., -1.)
    horizontal = vec3(4., 0., 0.)
    vertical = vec3(0., 2., 0.)
    origin = vec3(0., 0., 0.)

    focus = Sphere(
        center=vec3(0., 0., -1.),
        radius=0.5
    )
    ground = Sphere(
        center=vec3(0., -100.5, -1.),
        radius=100.0
    )
    world = HitableList([ground, focus])

    for y in range(height):
        for x in range(width):
            u, v = x / 200, y / 100
            direction = lower_left_corner + u*horizontal + v*vertical
            ray = Ray(origin, direction)
            pixels[x][y] = color(ray, world)

    return pixels


if __name__ == "__main__":
    pixels = get_example_pixels_np()

    P3Image(pixels).write('test.ppm')
