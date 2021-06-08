def hello():
    '''你好'''
    print("Hello world!")

print(hello)
print(type(hello))
print(hello.__doc__)
# <function hello at 0x000001D402AF39D0>
# <class 'function'>
# 你好
l = ["aa", "b", "ccc"]
print(sorted(l, key=len))
# ['b', 'aa', 'ccc']
persons = [('Jack chen', 16, 'actor'),
           ('Brus lee', 20, 'engineer')]


def formatPerson(person: tuple):
    return "name:%s,age:%s,actor:%s" % (person[0], str(person[1]), person[2])


formatPersons = list(map(formatPerson, persons))
print(formatPersons)
# ['name:Jack chen,age:16,actor:actor', 'name:Brus lee,age:20,actor:engineer']
persons = [('Jack chen', 16, 'actor'),
           ('Brus lee', 20, 'engineer')]

formatPersons = list(map(lambda person: "name:%s,age:%s,actor:%s" % (
    person[0], str(person[1]), person[2]), persons))
print(formatPersons)
# ['name:Jack chen,age:16,actor:actor', 'name:Brus lee,age:20,actor:engineer']
persons = [('Jack chen', 16, 'actor'),
           ('Brus lee', 20, 'engineer')]

formatPersons = ["name:%s,age:%s,actor%s" % (name,age,career) for name,age,career in persons]
print(formatPersons)
# ['name:Jack chen,age:16,actor:actor', 'name:Brus lee,age:20,actor:engineer']
from functools import reduce


def factorial(n):
    return reduce(lambda a, b: a*b, range(1, n+1))


print(factorial(1))
print(factorial(3))
print(factorial(5))
# 1
# 6
# 120
def hello():
    print("Hello world!")
class Test():
    pass
test = Test()

print(callable(hello))
print(callable(Test))
print(callable(test))
print(callable(len))
# True
# True
# False
# True
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self):
        print("Name:%s Age:%s" % (self.name, self.age))


JackChen = Person('Jack Chen', 16)
BrusLee = Person('Brus Lee', 20)
JackChen()
BrusLee()
# Name:Jack Chen Age:16
# Name:Brus Lee Age:20
def hello():
    print('Hello world!')


print(dir(hello))
# ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
def hello():
    print('Hello world!')


class Test():
    pass


print(set(dir(hello))-set(dir(Test)))
# {'__annotations__', '__kwdefaults__', '__qualname__', '__call__', '__globals__', '__code__', '__name__', '__get__', '__defaults__', '__closure__'}
def readFile(fileName, *, encoding='UTF-8'):
    content = ''
    with open(file=fileName, encoding=encoding, mode='r') as fopen:
        content = fopen.read()
    return content

print(readFile('test.txt'))
print(readFile('test.txt',encoding='UTF-8'))
print(readFile('test.txt','UTF-8'))
# 你好世界！

# 你好世界！

# Traceback (most recent call last):
#   File "d:\workspace\python\test\test.py", line 9, in <module>
#     print(readFile('test.txt','UTF-8'))
# TypeError: readFile() takes 1 positional argument but 2 were given
def person(name, age=15, *args, career='actor', **kwArgs):
    test = 'a function to test'


print(person.__defaults__)
print(person.__kwdefaults__)
print(person.__code__)
print(person.__code__.co_varnames)
# (15,)
# {'career': 'actor'}
# <code object person at 0x000002459B5BB5B0, file "d:\workspace\python\test\test.py", line 1>
# ('name', 'age', 'career', 'args', 'kwArgs', 'test')
from inspect import signature


def person(name, age=15, *args, career='actor', **kwArgs):
    test = 'a function to test'


personSig = signature(person)
print(personSig)
for name, param in personSig.parameters.items():
    print(param.kind, ':', name, '=', param.default)

# (name, age=15, *args, career='actor', **kwArgs)
# POSITIONAL_OR_KEYWORD : name = <class 'inspect._empty'>
# POSITIONAL_OR_KEYWORD : age = 15
# VAR_POSITIONAL : args = <class 'inspect._empty'>
# KEYWORD_ONLY : career = actor
# VAR_KEYWORD : kwArgs = <class 'inspect._empty'>
from inspect import signature


def person(name, age=15, *args, career='actor', **kwArgs):
    test = 'a function to test'


personSig = signature(person)
jackChen = {'name': 'Jack Chen', 'age': 16,
            'career': 'actor', 'other': 'no message'}
bindArgs = personSig.bind(**jackChen)
for name, value in bindArgs.arguments.items():
    print("%s=%s" % (name, value))
# name=Jack Chen
# age=16
# career=actor
# kwArgs={'other': 'no message'}
def person(name:str, age:int=15, *args:tuple, career:str='actor', **kwArgs:dict)->None:
    test = 'a function to test'

from inspect import signature


def person(name:str, age:int=15, *args:tuple, career:str='actor', **kwArgs:dict)->None:
    test = 'a function to test'


print(person.__annotations__)
# {'name': <class 'str'>, 'age': <class 'int'>, 'args': <class 'tuple'>, 'career': <class 'str'>, 'kwArgs': <class 'dict'>, 'return': None}
from inspect import signature


def person(name: str, age: int = 15, *args: tuple, career: str = 'actor', **kwArgs: dict) -> None:
    test = 'a function to test'


personSig = signature(person)
for name, param in personSig.parameters.items():
    print(param.annotation, name)
# <class 'str'> name
# <class 'int'> age
# <class 'tuple'> args
# <class 'str'> career
# <class 'dict'> kwArgs
from functools import reduce


def factorial(n):
    return reduce(lambda a, b: a*b, range(1, n+1))


print(factorial(1))
print(factorial(3))
print(factorial(5))
# 1
# 6
# 120
from functools import reduce
from operator import mul


def factorial(n):
    return reduce(mul, range(1, n+1))


print(factorial(1))
print(factorial(3))
print(factorial(5))
# 1
# 6
# 120
from functools import reduce
from operator import itemgetter
persons = [('Jack chen', 16, 'actor'), ('Brus lee', 20, 'engineer')]
getName = itemgetter(0)
getCareer = itemgetter(2)
for person in persons:
    print(getName(person),'->', getCareer(person))
# Jack chen -> actor
# Brus lee -> engineer
from functools import reduce
from operator import itemgetter
from pprint import pprint
persons = [('Jack chen', 16, 'engineer'), ('Brus lee', 20, 'actor')]
getCareer = itemgetter(2)
persons.sort(key=getCareer)
pprint(persons)
# [('Brus lee', 20, 'actor'), ('Jack chen', 16, 'engineer')]
from collections import namedtuple
from operator import attrgetter
person = namedtuple('person', 'name age career')
jackChen = person('Jack Chen', 16, 'actor')
brusLee = person('Brus Lee', 20, 'engineer')
getName = attrgetter('name')
getCareer = attrgetter('career')
print(getName(jackChen), '->', getCareer(jackChen))
print(getName(brusLee), '->', getCareer(brusLee))
# Jack Chen -> actor
# Brus Lee -> engineer
from collections import namedtuple
from operator import attrgetter
person = namedtuple('person', 'name age career favorites')
favorites = namedtuple('favorites', 'music dog cat')
jackChen = person('Jack Chen', 16, 'actor', favorites(False, True, True))
brusLee = person('Brus Lee', 20, 'engineer', favorites(False, False, True))
getName = attrgetter('name')
getCareer = attrgetter('career')
isLikeCat = attrgetter('favorites.cat')
isLikeDog = attrgetter('favorites.dog')
print(getName(jackChen), 'like' if isLikeDog(jackChen) else 'not like', 'dog')
print(getName(brusLee), 'like' if isLikeDog(brusLee) else 'not like', 'dog')
# Jack Chen like dog
# Brus Lee not like dog
from operator import methodcaller
toUpper = methodcaller('upper')
s = 'abcdefg'
print(s.upper())
print(toUpper(s))
# ABCDEFG
# ABCDEFG
def calculator(mode, x, y, opertor):
    if mode == 'simple':
        pass
    elif mode == 'math':
        pass
    else:
        pass
from functools import partial


def calculator(mode, x, y, opertor):
    if mode == 'simple':
        print('this is a simple calculator')
        pass
    elif mode == 'math':
        pass
    else:
        pass


simpleCal = partial(calculator, 'simple')
simpleCal(1, 2, 'add')
