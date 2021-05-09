from carrier import Carrier
from plane import Plane


class QueenElizabethCarrier(list):
    def loadPlanes(self, planes):
        '''加载飞机'''
        self.extend(planes)

    def land(self, plane: Plane):
        '''着陆飞机'''
        self.append(plane)
        print("{}从伊丽莎白女王号降落")

    def takeoff(self) -> Plane:
        '''起飞一架飞机，如果没有飞机了，返回False'''
        try:
            plane = self.pop()
        except IndexError:
            return False
        print("{}从伊丽莎白女王号起飞")
        return plane

    @classmethod
    def build(cls):
        '''建造航母'''
        return cls()

    def getAllPlanes(self):
        '''显示所有的飞机'''
        return self

    def __str__(self):
        string = ""
        for plane in self:
            string += "{} ".format(plane)
        return string

Carrier.register(QueenElizabethCarrier)
