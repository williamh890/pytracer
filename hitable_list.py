from hitable import Hitable
from utils import Range

import numpy as np


class HitableList(Hitable):
    def __init__(self, objects):
        self.objects = objects

    def does_hit(self, ray, t_range):
        closest_object = None

        for thing in self.objects:
            maybe_hit = thing.does_hit(ray, t_range)

            if maybe_hit is None:
                continue

            closest_object = maybe_hit
            t_range = Range(0, closest_object.time)

        return closest_object

    def find_hits(self, rays, t_range):
        width, height, _ = rays.shape
        closest_hits = np.zeros((width, height, 1), dtype="bool")

        for thing in self.objects:
            hits, ts, positions, normals = thing.any_hits(rays, t)


        print(closest_hits.shape)
