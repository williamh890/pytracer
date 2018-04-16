from utils import random_in_unit_sphere, reflect, normalized
from ray import Ray

import numpy as np
from abc import abstractmethod


class Material:
    @abstractmethod
    def scatter(self, ray_in, hit):
        pass


class Lambertian(Material):
    def __init__(self, albedo):
        self.albedo = albedo

    def scatter(self, ray_in, hit):
        target = hit.p + hit.normal + random_in_unit_sphere()

        new_ray = Ray(
            hit.p,
            target - hit.p,
            attenuation=self.albedo
        )

        return new_ray


class Metal(Material):
    def __init__(self, albedo):
        self.albedo = albedo

    def scatter(self, ray_in, hit):
        reflected = reflect(normalized(ray_in.direction), hit.normal)

        scattered = Ray(
            hit.p,
            reflected,
            attenuation=self.albedo
        )

        if np.dot(scattered.direction, hit.normal) > 0:
            return scattered
