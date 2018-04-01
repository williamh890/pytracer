import numpy as np
from utils import vec3

zeroVec = vec3(0., 0., 0.)


class Ray:
    def __init__(self, origin=zeroVec, direction=zeroVec):
        self.origin = origin
        self.direction = direction

    def point_at_parameter(self, t):
        return self.origin + t * self.direction

    def does_hit_sphere(self, s):
        oc = self.origin - s.center
        d = self.direction
        a = np.dot(d, d)
        b = 2. * np.dot(oc, d)
        c = np.dot(oc, oc) - s.radius**2
        discriminate = b**2 - 4*a*c

        if discriminate < 0.:
            return -1.

        return (-b - discriminate**.5) / (2. * a)
