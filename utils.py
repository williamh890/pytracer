import numpy as np


def normalized(a, axis=-1, order=2):
    l2 = np.atleast_1d(np.linalg.norm(a, order, axis))
    l2[l2 == 0] = 1
    return a / np.expand_dims(l2, axis)


def vec3(x, y, z):
    return np.array([x, y, z])


def pixel(r, g, b):
    return vec3(r, g, b)

class Sphere:
    def __init__(self, center=None, radius=None):
        self.center = center
        self.radius = radius

