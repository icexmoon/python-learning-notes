a = 1
b = 1
print(id(a))
print(id(b))
# 1229568305456
# 1229568305456
a = [1,2,3]
b = [1,2,3]
c = b
print(a == b)
print(a is b)
print(b is c)
# True
# False
# True
a = (1, 2, 3)
b = (1, 2, 3)
c = b
print(a == b)
print(a is b)
print(b is c)
# True
# True
# True
a = (1, 2, 3, ['a', 'b'], ('a', 'b'))
b = a
a[-2].append('c')
print(a)
print(b)
# (1, 2, 3, ['a', 'b', 'c'], ('a', 'b'))
# (1, 2, 3, ['a', 'b', 'c'], ('a', 'b'))
a = [1, 2, 3]
b = list(a)
a[-1] = 5
print(a)
print(b)
# [1, 2, 5]
# [1, 2, 3]
a = [1, 2, 3, ['a', 'b']]
b = list(a)
a[-1].append('c')
a[-2] = 5
print(a)
print(b)
# [1, 2, 5, ['a', 'b', 'c']]
# [1, 2, 3, ['a', 'b', 'c']]
a = [1, 2, 3, ['a', 'b']]
b = a[:]
a[-1].append('c')
a[-2] = 5
print(a)
print(b)
# [1, 2, 5, ['a', 'b', 'c']]
# [1, 2, 3, ['a', 'b', 'c']]
import copy
a = [1, 2, 3, ['a', 'b']]
b = copy.copy(a)
c = copy.deepcopy(a)
a[-1].append('c')
a[-2] = 5
print(a)
print(b)
print(c)
# [1, 2, 5, ['a', 'b', 'c']]
# [1, 2, 3, ['a', 'b', 'c']]
# [1, 2, 3, ['a', 'b']]
import copy
a = [1,2]
b = [a,1,2]
a.insert(1, b)
print(a)
c = copy.deepcopy(a)
print(c)
# [1, [[...], 1, 2], 2]
# [1, [[...], 1, 2], 2]
def changeNum(num):
    num = 2


num = 1
changeNum(num)
print(num)
# 1
def changeList(lst: list):
    lst = [1, 2, 3]


def changeList2(lst: list):
    lst.clear()
    lst.extend([1, 2, 3])


lst = [4, 5, 6]
changeList(lst)
print(lst)
changeList2(lst)
print(lst)
class Bus():
    def __init__(self, people: list = []):
        self.people = people

    def up(self, newOne: str):
        self.people.append(newOne)

    def down(self, leaved: str):
        self.people.remove(leaved)

    def __repr__(self):
        return "bus->%r"%self.people

bus1 = Bus(["Jack Chen","Brus Lee","Xiao Min"])
bus2 = Bus(["Han Meimei","Li Lei"])
bus1.down("Jack Chen")
bus2.up("Jack Chen")
print(bus1)
print(bus2)
# bus->['Brus Lee', 'Xiao Min']
# bus->['Han Meimei', 'Li Lei', 'Jack Chen']
class Bus():
    def __init__(self, people: list = []):
        self.people = people

    def up(self, newOne: str):
        self.people.append(newOne)

    def down(self, leaved: str):
        self.people.remove(leaved)

    def __repr__(self):
        return "bus->%r"%self.people

bus1 = Bus()
bus2 = Bus()
bus1.up("Jack Chen")
bus1.up("Han Meimei")
bus1.up("Brus Lee")
print(bus1)
print(bus2)
# bus->['Jack Chen', 'Han Meimei', 'Brus Lee']
# bus->['Jack Chen', 'Han Meimei', 'Brus Lee']
print(dir(Bus.__init__))
print(Bus.__init__.__defaults__)
# ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
# (['Jack Chen', 'Han Meimei', 'Brus Lee'],)
print(bus1.people is bus2.people)
# True
class Bus():
    def __init__(self, people: list = None):
        if (people is None):
            self.people = []
        else:
            self.people = people

    def up(self, newOne: str):
        self.people.append(newOne)

    def down(self, leaved: str):
        self.people.remove(leaved)

    def __repr__(self):
        return "bus->%r"%self.people

bus1 = Bus()
bus2 = Bus()
bus1.up("Jack Chen")
bus1.up("Han Meimei")
bus1.up("Brus Lee")
print(bus1)
print(bus2)
print(bus1.people is bus2.people)
# bus->['Jack Chen', 'Han Meimei', 'Brus Lee']
# bus->[]
# False
import weakref
a = {1, 2, 3}
b = a


def varDisabled():
    print('var is disabled')


varRef = weakref.finalize(a, varDisabled)
del(a)
print(varRef.alive)
del(b)
print(varRef.alive)
# True
# var is disabled
# False
from weakref import WeakValueDictionary,WeakKeyDictionary,WeakSet


class Person():
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return "Person(%s)" % self.name

people = {'Jack Chen': Person('Jack Chen'), 'Brus Lee': Person(
    'Brus Lee'), 'Han Meimei': Person('Han Meimei')}
wvDict = WeakValueDictionary(people)
print(sorted(wvDict.keys()))
for k, v in wvDict.items():
    print("%s:%r" % (k, v))
del people
print(sorted(wvDict.keys()))
print(v)
del v
print(sorted(wvDict.keys()))
# ['Brus Lee', 'Han Meimei', 'Jack Chen']
# Jack Chen:Person(Jack Chen)
# Brus Lee:Person(Brus Lee)
# Han Meimei:Person(Han Meimei)
# ['Han Meimei']
# Person(Han Meimei)
# []
a = 1
b = 1
print(a is b)
a = (1, 2, 3)
b = (1, 2, 3)
print(a is b)
# True
# True
a = (1,2,3)
b = tuple(a)
print(a is b)
# True
tuple1 = tuple([1,2,3])
tuple2 = tuple([1,2,3])
print(tuple1 is tuple2)
a = [1,2,3]
tuple1 = tuple(a)
tuple2 = tuple(a)
print(tuple1 is tuple2)
# False
# False
a = (1,2,3,[1,2])
b = (1,2,3,[1,2])
print(a is b)
# False
