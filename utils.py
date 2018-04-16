import numpy as np
import collections
from ABC import abstractmethod


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


class Material:
    @abstractmethod
    def scatter(ray_in, hit):
        pass


class Lambertian(Material):
    def __init__(self, albedo):
        self.albedo = self.albedo

    def scatter(ray_in, hit):
        target = hit.p + hit.normal + random_in_unit_sphere()

        new_ray = Ray(
            hit.p,
            target - hit.p,
            attenuation=self.albedo
        )

        return new_ray


class Metal(Material):
    def __init__(self, albedo):
        self.albedo = self.albedo

    def scatter(ray_in, hit):
        reflected = reflect(normalized(ray_in.direction), hit.normal)

        scattered = Ray(
            hit.p,
            reflected,
            attenuation=self.albedo
        )

        if np.dot(scattered.direction, rec.normal) > 0:
            return scattered


Hit = collections.namedtuple('Hit', ['time', 'p', 'normal', 'material'])
Range = collections.namedtuple('Range', ['min', 'max'])
