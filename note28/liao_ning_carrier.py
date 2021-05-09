from carrier import Carrier
from plane import Plane


class LiaoNingCarrier(Carrier):
    def __init__(self):
        self._garage = []

    def land(self, plane: Plane):
        self._garage.append(plane)
        print("{}在辽宁号着陆".format(plane))

    def takeoff(self) -> Plane:
        try:
            plane = self._garage.pop(0)
        except IndexError:
            return False
        print("{}从辽宁号起飞".format(plane))
        return plane

    @classmethod
    def build(cls):
        return cls()

    def loadPlanes(self, planes):
        self._garage.extend(planes)

    def getAllPlanes(self):
        return self._garage
