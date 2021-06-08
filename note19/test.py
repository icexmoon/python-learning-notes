listA = ['a', 'b', 'c']
listB = [1, 2, 3]
result = [(a, b) for a in listA for b in listB]
print(result)
# [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]
listA = ['a', 'b', 'c']
listB = [1, 2, 3]
results = []
for result in ((a, b) for a in listA for b in listB):
    results.append(result)
print(results)
# [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]
from random import randint
listA = [randint(1, 100) for i in range(0, 10)]
print(listA)
listA.sort()
print(listA)
# [92, 52, 95, 27, 67, 97, 56, 22, 72, 24]
# [22, 24, 27, 52, 56, 67, 72, 92, 95, 97]
from random import randint
listA = [randint(1, 100) for i in range(0, 10)]
print(sorted(listA))
print(listA)
# [10, 13, 15, 43, 46, 62, 77, 80, 90, 97]
# [10, 13, 77, 46, 43, 15, 80, 62, 97, 90]
listA = ["sdfsdf", "eaw", "dfwe", "aqwe", "kersfsq"]
print(sorted(listA))
print(sorted(listA, key=len))
# ['aqwe', 'dfwe', 'eaw', 'kersfsq', 'sdfsdf']
# ['eaw', 'dfwe', 'aqwe', 'sdfsdf', 'kersfsq']
import bisect
listA = [0, 1, 2, 3, 4, 5, 6]
index = bisect.bisect(listA, 3)
indexL = bisect.bisect_left(listA, 3)
indexR = bisect.bisect_right(listA, 3)
print(index)
print(indexL)
print(indexR)
# 4
# 3
# 4
import bisect
listA = [0, 1, 2, 3, 4, 5, 6]
bisect.insort(listA, 3)
print(listA)
# [0, 1, 2, 3, 3, 4, 5, 6]
import random
import bisect


def bisectSort(listA: list) -> list:
    sortedList = []
    for num in listA:
        bisect.insort(sortedList, num)
    return sortedList


listA = [random.randint(1, 100) for i in range(0, 10)]
print(listA)
print(bisectSort(listA))
# [96, 43, 58, 15, 2, 88, 56, 56, 41, 20]
# [2, 15, 20, 41, 43, 56, 56, 58, 88, 96]
listA = ['a', 'b', 'c', 'd', 'e']
listA[1:4] = ['d', 'c', 'b']
print(listA)
# ['a', 'd', 'c', 'b', 'e']
listA = ['a', 'b', 'c', 'd', 'e']
listA[::2] = ['z', 'z', 'z']
print(listA)
# ['z', 'b', 'z', 'd', 'z']
from collections import namedtuple
Person = namedtuple("Person", ("name", "age", "career", "favorite"))
Jack = Person("Jack chen", 17, "actor", ("swimming", "running"))
Brus = Person("Brus Lee", 20, "engineer", ("football", "table tennis"))
print(Jack)
print(Brus)
print(Jack.name)
print(Jack.favorite)
print(Jack[1])
dictJack = Jack._asdict()
print(dictJack)
# Person(name='Jack chen', age=17, career='actor', favorite=('swimming', 'running'))
# Person(name='Brus Lee', age=20, career='engineer', favorite=('football', 'table tennis'))
# Jack chen
# ('swimming', 'running')
# 17
# {'name': 'Jack chen', 'age': 17, 'career': 'actor', 'favorite': ('swimming', 'running')}
tupleA = ("Jack Chen", 16, "engineer", ("football", "table tennis"))
name, *_, (favorite1, favorite2) = tupleA
print(name, favorite1, favorite2)
# Jack Chen football table tennis
persons = [("Jack Chen", 16, "engineer", ("football", "table tennis")),
           ("Brus Lee", 20, "actor", ("swimming", "running"))]
for name, *_, (favorite1, favorite2) in persons:
    print(name, favorite1, favorite2)
# Jack Chen football table tennis
# Brus Lee swimming running
jack = ("Jack Chen", 16, "engineer", ["football", "table tennis"])
# jack[-1] += ["swimming"]
# print(jack)
# Traceback (most recent call last):
#   File "D:\workspace\python\python-learning-notes\note19\test.py", line 99, in <module>
#     jack[-1] += ["swimming"]
# TypeError: 'tuple' object does not support item assignment
jack = ("Jack Chen", 16, "engineer", ["football", "table tennis"])
jack[-1].extend(["swimming"])
print(jack)
# ('Jack Chen', 16, 'engineer', ['football', 'table tennis', 'swimming'])
from collections import deque
myQuen = deque(maxlen=10)
listNum = [i for i in range(0,20)]
myQuen.extend(listNum[:10])
print(myQuen)
myQuen.extend(listNum[10:13])
print(myQuen)
myQuen.extendleft(listNum[13:16])
print(myQuen)
myQuen.pop()
myQuen.insert(2,0)
print(myQuen)
# deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
# deque([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], maxlen=10)
# deque([15, 14, 13, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
# deque([15, 14, 0, 13, 3, 4, 5, 6, 7, 8], maxlen=10)
import array
import random
a = array.array('i', (random.randint(1, 100) for i in range(0, 1000)))
print(a[-1])
fopen = open(mode='wb', file='array.file')
a.tofile(fopen)
fopen.close()
b = array.array('i')
fopen = open(mode='rb', file='array.file')
b.fromfile(fopen, 1000)
fopen.close()
print(b[-1])
print(a == b)
# 22
# 22
# True
import numpy
nArray = numpy.arange(20)
print(nArray)
print(type(nArray))
print(nArray.shape)
nArray.shape=(4,5)
print(nArray)
print(nArray[2])
print(nArray[:,3])
print(nArray[2][3])
print(nArray.transpose())
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
# <class 'numpy.ndarray'>
# (20,)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]]
# [10 11 12 13 14]
# [ 3  8 13 18]
# 13
# [[ 0  5 10 15]
#  [ 1  6 11 16]
#  [ 2  7 12 17]
#  [ 3  8 13 18]
#  [ 4  9 14 19]]