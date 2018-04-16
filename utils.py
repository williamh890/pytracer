import numpy as np
import collections
import random


def normalized(a, axis=-1, order=2):
    l2 = np.atleast_1d(np.linalg.norm(a, order, axis))
    l2[l2 == 0] = 1
    return a / np.expand_dims(l2, axis)[0]


def vec3(x, y, z):
    return np.array([x, y, z], dtype="float")


def pixel(r, g, b):
    return vec3(r, g, b)


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


def reflect(v, n):
    return v - 2 * np.dot(v, n) * v


Hit = collections.namedtuple('Hit', ['time', 'p', 'normal', 'material'])
Range = collections.namedtuple('Range', ['min', 'max'])
