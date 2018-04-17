from abc import abstractmethod


class Hitable:
    @abstractmethod
    def did_hit(ray, t_range):
        pass
