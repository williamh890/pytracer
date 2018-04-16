from hitable import Hitable
from utils import Hit, normalized, vec3

import numpy as np
import noise
from abc import abstractmethod


class Sphere(Hitable):
    def __init__(self, center=None, radius=None, material=None):
        self.center = center
        self.radius = radius
        self.material = material

    def does_hit(self, ray, t_range):
        oc = ray.origin - self.center
        d = ray.direction
        a = np.dot(d, d)
        b = np.dot(oc, d)
        c = np.dot(oc, oc) - self.radius**2
        discriminate = b**2 - a*c

        if discriminate > 0.:
            diff = (b*b-a*c)**.5
            temp = (-b - diff) / a

            if temp < t_range.max and temp > t_range.min:
                p = ray.point_at_parameter(temp)
                normal = self.get_normal(p)

                return Hit(temp, p, normal, self.material)

            temp = (-b + diff) / a
            if temp < t_range.max and temp > t_range.min:
                p = ray.point_at_parameter(temp)
                normal = self.get_normal(p)

                return Hit(temp, p, normal, self.material)

        return None

    @abstractmethod
    def get_normal(self, p):
        pass


class RegularSphere(Sphere):
    def get_normal(self, p):
        return (p - self.center) / self.radius


class PerlinSphere1(Sphere):
    def get_normal(self, p):
        return (p - self.center) / self.radius *    \
            noise.pnoise2(p[0] / 3, 10 * p[1], 10) * 100.


class PerlinSphere2(Sphere):
    def get_normal(self, p):
        return vec3(182, 155, 76) /  \
            noise.pnoise1(p[2], 3) * .01


class CrazyPerlin(Sphere):
    def get_normal(self, p):
        p = p * 10
        return (p - self.center) / self.radius * \
            noise.pnoise3(p[0], p[1], p[2], 1)
