from ray import Ray
from collections import namedtuple

CameraData = namedtuple("CameraData", [
    'lower_left_corner',
    'horizontal',
    'vertical',
    'origin'
])


class Camera(CameraData):
    def get_ray(self, u, v):
        direction = self.lower_left_corner + u*self.horizontal + v*self.vertical

        return Ray(self.origin, direction)
