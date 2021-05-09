import abc
from collections import namedtuple
from plane import Plane

class Carrier(abc.ABC):
    @abc.abstractmethod
    def loadPlanes(self, planes):
        '''加载飞机'''

    @abc.abstractmethod
    def land(self, plane: Plane):
        '''着陆飞机'''

    @abc.abstractmethod
    def takeoff(self) -> Plane:
        '''起飞一架飞机，如果没有飞机了，返回False'''

    @classmethod
    @abc.abstractmethod
    def build(cls):
        '''建造航母'''

    def getAllPlanes(self):
        '''显示所有的飞机'''
        planes = []
        while True:
            plane = self.takeoff()
            if plane != False:
                planes.append(plane)
            else:
                break
        for plane in planes:
            self.land(plane)
        return planes

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Carrier:
            for baseCls in C.__mro__:
                allFuncs = baseCls.__dict__.keys()
                mustFuncs = {"loadPlanes","land","takeoff","build","getAllPlanes"}
                if set(mustFuncs)<=set(allFuncs):
                    return True
        return NotImplemented
