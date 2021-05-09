from plane import Plane
class SFCarrier():
    def loadPlanes(self, planes):
        '''加载飞机'''
        pass

    def land(self, plane: Plane):
        '''着陆飞机'''
        pass

    def takeoff(self) -> Plane:
        '''起飞一架飞机，如果没有飞机了，返回False'''
        pass

    @classmethod
    def build(cls):
        '''建造航母'''
        return cls()

    def getAllPlanes(self):
        '''显示所有的飞机'''
        return []