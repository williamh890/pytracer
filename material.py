from utils import random_in_unit_sphere, reflect, \
    normalized, vec3, refract, schlick
from ray import Ray

import numpy as np
import random
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
            target - hit.p
        )

        return new_ray, self.albedo


class Metal(Material):
    def __init__(self, albedo):
        self.albedo = albedo

    def scatter(self, ray_in, hit):
        reflected = reflect(normalized(ray_in.direction), hit.normal)

        scattered = Ray(
            hit.p,
            reflected
        )

        return scattered, self.albedo


class Dielectric(Material):
    def __init__(self, ri):
        self.ref_idx = ri

    def scatter(self, ray_in, hit):
        reflected = reflect(ray_in.direction, hit.normal)
        attenuation = vec3(1., 1., 1.)

        if np.dot(ray_in.direction, hit.normal) > 0:
            outward_normal = -hit.normal
            ni_over_nt = self.ref_idx
            cosine = self.ref_idx * \
                np.dot(ray_in.direction, hit.normal) / \
                np.linalg.norm(ray_in.direction)
        else:
            outward_normal = hit.normal
            ni_over_nt = 1. / self.ref_idx
            cosine =        \
                -np.dot(ray_in.direction, hit.normal) / \
                np.linalg.norm(ray_in.direction)

        try_refract = refract(
            ray_in.direction,
            outward_normal,
            ni_over_nt
        )

        if try_refract is not None:

            out = Ray(hit.p, try_refract)

            reflect_prob = schlick(cosine, self.ref_idx)

            if random.uniform(0, 1) <= reflect_prob:
                return out, attenuation

        out = Ray(hit.p, reflected)

        return out, attenuation
