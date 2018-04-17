from p3 import P3Image
from utils import \
    normalized, vec3, pixel, \
    Range, random_in_unit_sphere

from material import Metal, Lambertian, Dielectric

from sphere import RegularSphere
from hitable_list import HitableList
from camera import Camera
from ray import Ray

import numpy as np
import sys
import random
from multiprocessing import Pool
# random.uniform(0, 1)

WIDTH, HEIGHT, SAMPLES, MAX_DEPTH = 640, 480, 10, 5
INFINITY = sys.float_info.max


def color(ray, world, depth=0):
    t_range = Range(0.001, INFINITY)
    hit = world.does_hit(ray, t_range)

    if hit is not None:
        if depth >= MAX_DEPTH:
            return vec3(0, 0, 0)

        scattered = hit.material.scatter(ray, hit)
        if scattered is None:
            return vec3(0, 0, 0)

        new_ray, attenuation = scattered
        return attenuation * color(new_ray, world, depth + 1)

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
        center=vec3(0., 0., -2.),
        radius=.8,
        material=Lambertian(vec3(.1, .2, .5))
    )

    focus3 = RegularSphere(
        center=vec3(1., 1., -2.),
        radius=.6,
        material=Metal(vec3(.2, .2, .8))
    )

    focus1 = RegularSphere(
        center=vec3(1., 0., -1.),
        radius=0.5,
        material=Dielectric(1.5)
    )

    focus2 = RegularSphere(
        center=vec3(-1., 0., -1.),
        radius=0.5,
        material=Metal(vec3(.8, .6, .2))
    )

    ground = RegularSphere(
        center=vec3(0., -100.5, -1.),
        radius=100.0,
        material=Lambertian(vec3(.8, .8, .0))
    )
    world = HitableList([ground, focus, focus1, focus2, focus3])

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
            u = (x + random.uniform(0, 1.)) / WIDTH
            v = (y + random.uniform(0, 1.)) / HEIGHT

            ray = camera.get_ray(u, v)
            total_samples += color(ray, world)

        col[y] = (total_samples / SAMPLES) ** .5

    return col


if __name__ == "__main__":
    pixels = get_pixels()

    P3Image(pixels).write('test.ppm')
