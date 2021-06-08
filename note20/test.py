from dis import dis
dis("a=[1,2,3]")
dis("a=list(1,2,3)")
#输出
#   1           0 BUILD_LIST               0
#               2 LOAD_CONST               0 ((1, 2, 3))
#               4 LIST_EXTEND              1
#               6 STORE_NAME               0 (a)        
#               8 LOAD_CONST               1 (None)
#              10 RETURN_VALUE
#   1           0 LOAD_NAME                0 (list)
#               2 LOAD_CONST               0 (1)
#               4 LOAD_CONST               1 (2)
#               6 LOAD_CONST               2 (3)
#               8 CALL_FUNCTION            3
#              10 STORE_NAME               1 (a)
#              12 LOAD_CONST               3 (None)
#              14 RETURN_VALUE
string = "Hellow World"
charCounter = {}
for char in string:
    if char not in charCounter:
        charCounter[char] = 0
    charCounter[char] += 1
print(charCounter)
#输出
#{'H': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1}
string = "Hellow World"
charCounter = {}
for char in string:
    charCounter[char] = charCounter.get(char, 0)+1
print(charCounter)
# 输出
#{'H': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1}
string = "Hellow World"
charCounter = {}
for char in string:
    charCounter.setdefault(char, 0)
    charCounter[char] += 1
print(charCounter)
# 输出
#{'H': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1}
from collections import defaultdict
def setZero():
    return 0
charCounter = defaultdict(setZero)
string = "Hellow world!"
for char in string:
    charCounter[char] += 1
print(charCounter)
#输出
#defaultdict(<function setZero at 0x000001E8D5B93940>, {'H': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 2, ' ': 1, 'r': 1, 'd': 1, '!': 1})
class myDefaultDict(dict):

    def setDefault(self, default):
        self.default = default

    def __missing__(self, key):
        self[key] = self.default
        return self.default


counter = myDefaultDict()
counter.setDefault(0)
string = "Hellow world!"
for char in string:
    counter[char] += 1
print(counter)
#输出
#{'H': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 2, ' ': 1, 'r': 1, 'd': 1, '!': 1}
from collections import UserDict


class MyDefaultDict(UserDict):
    def setdefault(self, default):
        self.defaultVal = default

    def __missing__(self, key):
        self.data[key] = self.defaultVal
        return self.defaultVal


charCounter = MyDefaultDict()
charCounter.setdefault(0)
string = "Hellow world!"
for char in string:
    charCounter[char] += 1
print(charCounter)
#{'H': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 2, ' ': 1, 'r': 1, 'd': 1, '!': 1}
from collections import Counter
charCounter = Counter("Hellow world!")
print(charCounter)
# 输出
# Counter({'l': 3, 'o': 2, 'w': 2, 'H': 1, 'e': 1, ' ': 1, 'r': 1, 'd': 1, '!': 1})
setA = {1, 2, 3, 4, 5, 6}
setB = {2, 5, 9, 10}
print(setA & setB)
print(setA.intersection(setB))
listA = [2, 5, 5, 9, 9, 10]
print(setA.intersection(listA))
# 输出
# {2, 5}
# {2, 5}
# {2, 5}
setA = {1, 2, 3, 4, 5, 6}
setB = {2, 5, 9, 10}
print(setA | setB)
print(setA.union(setB))
listA = [2, 5, 5, 9, 9, 10]
print(setA.union(listA))
# 输出
# {1, 2, 3, 4, 5, 6, 9, 10}
# {1, 2, 3, 4, 5, 6, 9, 10}
# {1, 2, 3, 4, 5, 6, 9, 10}
setA = {1, 2, 3, 4, 5, 6}
setB = {2, 5, 9, 10}
print(setA - setB)
print(setA.difference(setB))
listA = [2, 5, 5, 9, 9, 10]
print(setA.difference(listA))
# 输出
# {1, 3, 4, 6}
# {1, 3, 4, 6}
# {1, 3, 4, 6}
setA = {1, 2, 3, 4, 5, 6}
setB = {2, 5, 9, 10}
print(setA ^ setB)
print(setA.symmetric_difference(setB))
listA = [2, 5, 5, 9, 9, 10]
print(setA.symmetric_difference(listA))
# 输出
# {1, 3, 4, 6, 9, 10}
# {1, 3, 4, 6, 9, 10}
# {1, 3, 4, 6, 9, 10}