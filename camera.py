from ray import Ray
from collections import namedtuple

import numpy as np

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

    def get_rays(self, u_arr, v_arr):
        us = np.dstack((u_arr, u_arr, u_arr))
        vs = np.dstack((v_arr, v_arr, v_arr))
        directions = us*self.horizontal + vs * \
            self.vertical + self.lower_left_corner

        return directions
