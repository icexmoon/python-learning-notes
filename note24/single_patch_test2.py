import numbers
import inspect
from functools import singledispatch


@singledispatch
def showEverything(obj):
    print('this is a object:%r' % obj)


@showEverything.register(numbers.Integral)
def _(intVar: int):
    print('this is a integer:%s' % intVar)


@showEverything.register(str)
def _(strVar: str):
    print('this is a string:%s' % strVar)


showEverything(1)
showEverything('hellow wolrd!')
showEverything(len)