from p3 import P3Image
from utils import normalized, vec3, pixel, Range
from sphere import RegularSphere
from hitable_list import HitableList
from camera import Camera

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


def get_pixels():
    pixels = np.empty([WIDTH, HEIGHT, 3], dtype="float")
    width, height, channels = pixels.shape

    lower_left_corner = vec3(-2., -1., -1.)
    horizontal = vec3(4., 0., 0.)
    vertical = vec3(0., 2., 0.)
    origin = vec3(0., 0., 0.)

    camera = Camera(
        lower_left_corner,
        horizontal,
        vertical,
        origin,
    )

    focus = RegularSphere(
        center=vec3(0., 0., -1.),
        radius=0.5
    )
    ground = RegularSphere(
        center=vec3(0., -100.5, -1.),
        radius=100.0
    )
    world = HitableList([ground, focus])

    for y in range(height):
        for x in range(width):
            u, v = x / 200, y / 100
            ray = camera.get_ray(u, v)
            c = color(ray, world)

            pixels[x][y] = c

    return pixels


if __name__ == "__main__":
    pixels = get_pixels()

    P3Image(pixels).write('test.ppm')
