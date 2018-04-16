import numpy as np
from utils import vec3

zeroVec = vec3(0., 0., 0.)


class Ray:
    def __init__(self, origin=zeroVec, direction=zeroVec, attenuation=None):
        self.origin = origin
        self.direction = direction
        self.attenuation = attenuation

    def point_at_parameter(self, t):
        return self.origin + t * self.direction
