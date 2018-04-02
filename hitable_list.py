from hitable import Hitable
from utils import Range


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
