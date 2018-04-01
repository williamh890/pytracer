from hitable import Hitable
from utils import Hit

import numpy as np


class Sphere(Hitable):
    def __init__(self, center=None, radius=None):
        self.center = center
        self.radius = radius
        pass

    def does_hit(self, ray, t_range):
        oc = ray.origin - self.center
        d = ray.direction
        a = np.dot(d, d)
        b = 2. * np.dot(oc, d)
        c = np.dot(oc, oc) - self.radius**2
        discriminate = b**2 - 4*a*c

        if discriminate > 0.:
            diff = (b*b-a*c)**.5
            temp = (-b - diff) / a

            if temp < t_range.max and temp > t_range.min:
                p = ray.point_at_parameter(temp)
                normal = (p - self.center) / self.radius
                return Hit(temp, p, normal)

            temp = (-b + diff) / a
            if temp < t_range.max and temp > t_range.min:
                p = ray.point_at_parameter(temp)
                normal = (p - self.center) / self.radius
                return Hit(temp, p, normal)

        return None
