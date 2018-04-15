from p3 import P3Image
from utils import normalized, vec3, pixel, Range
from sphere import RegularSphere
from hitable_list import HitableList
from camera import Camera
from ray import Ray

import numpy as np
import sys
import random
from multiprocessing import Pool
# random.uniform(0, 1)

WIDTH, HEIGHT, SAMPLES = 200, 100, 20
INFINITY = sys.float_info.max


def color(ray, world):
    t_range = Range(0., INFINITY)
    hit = world.does_hit(ray, t_range)

    if hit is not None:
        target = hit.p + hit.normal + random_in_unit_sphere()
        newRay = Ray(hit.p, target-hit.p)

        return .5 * color(newRay, world)

    unit_dir = normalized(ray.direction)
    t = .5 * (unit_dir[1] + 1.)

    return (1. - t) * vec3(1., 1., 1.) + \
        t * vec3(.5, .7, 1.)


def random_in_unit_sphere():
    ones = vec3(1., 1., 1.)
    while True:
        p = 2 * vec3(
            random.uniform(-1., 1.),
            random.uniform(-1., 1.),
            random.uniform(-1., 1.)
        ) - ones

        if p.dot(p) >= 1.0:
            return p


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

    args = [
        [x, world, camera] for x in range(width)
    ]

    with Pool(8) as p:
        rows = p.map_async(trace_column, args).get()

    for x in range(WIDTH):
        pixels[x] = rows[x]

    return pixels


def trace_column(args):
    x, world, camera = args

    if x % 20 == 0:
        print(x)

    col = np.empty([HEIGHT, 3], dtype="float")
    for y in range(HEIGHT):
        total_samples = vec3(0, 0, 0)
        for _ in range(SAMPLES):
            u = (x + random.uniform(0, 1.)) / 200
            v = (y + random.uniform(0, 1.)) / 100

            ray = camera.get_ray(u, v)
            total_samples += color(ray, world)

        col[y] = total_samples / SAMPLES

    return col


if __name__ == "__main__":
    pixels = get_pixels()

    P3Image(pixels).write('test.ppm')
