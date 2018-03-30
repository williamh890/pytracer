import numpy as np
from utils import normalized, vec3, Sphere

zeroVec = np.array([0., 0., 0.])


class Ray:
    def __init__(self, origin=zeroVec, direction=zeroVec):
        self.origin = origin
        self.direction = direction

        self.sphere = Sphere(
            center=vec3(0., 0., -1.),
            radius=0.5
        )

    def point_at_parameter(time):
        return self.origin + t * self.position

    @property
    def color(self):
        if (self.does_hit_sphere(self.sphere)):
            return vec3(1., 0., 0.)

        unit_dir = normalized(self.direction)[0]
        t = .5 * (unit_dir[1] + 1.)

        return (1. - t) * np.array([1., 1., 1.]) + \
            t * np.array([.5, .7, 1.])

    def does_hit_sphere(self, s):
        oc = self.origin - s.center
        d = self.direction
        a = np.dot(d, d)
        b = 2. * np.dot(oc, d)
        c = np.dot(oc, oc) - s.radius**2
        discriminate = b**2 - 4*a*c

        return discriminate > 0
