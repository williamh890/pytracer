from abc import abstractmethod


class Hitable:
    def __init__(self):
        pass

    @abstractmethod
    def did_hit(ray, t_range):
        pass
