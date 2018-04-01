from hitable import Hitable


class HitableList(Hitable):
    def __init__(self, objects):
        self.objects = objects

    def does_hit(self, ray, t_range):
        closest_object, closest_hit = t_range.max, None

        for thing in self.objects:
            maybe_hit = thing.does_hit(ray, t_range)

            if maybe_hit is not None:
                closest_hit = maybe_hit
                closest_object = closest_hit.time

        return closest_hit
