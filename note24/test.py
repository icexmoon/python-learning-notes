registed = []
def register(func):
    registed.append(func)
    print(str(func),"is registed")
    return func

@register
def test1():
    print('this is test1 function')

@register
def test2():
    print('this is test2 function')

print("main function begin")
print(registed)
test1()
test2()
# <function test1 at 0x000002196EF73A60> is registed
# <function test2 at 0x000002196EF73B80> is registed
# main function begin
# [<function test1 at 0x000002196EF73A60>, <function test2 at 0x000002196EF73B80>]
# this is test1 function
# this is test2 function
registed = []
def register(func):
    registed.append(func)
    print(str(func),"is registed")
    return func

def test1():
    print('this is test1 function')
test1 = register(test1)

def test2():
    print('this is test2 function')
test2 = register(test2)

print("main function begin")
print(registed)
test1()
test2()
# <function test1 at 0x000002196EF73A60> is registed
# <function test2 at 0x000002196EF73B80> is registed
# main function begin
# [<function test1 at 0x000002196EF73A60>, <function test2 at 0x000002196EF73B80>]
# this is test1 function
# this is test2 function
numbers = []


def per(num: int) -> float:
    numbers.append(num)
    return sum(numbers)/len(numbers)

print(per(1))
print(per(5))
print(per(10))
# 1.0
# 3.0
# 5.333333333333333
total = 0
nums = 0

def per(num: int) -> float:
    total += num
    nums += 1
    return total/nums

print(per(1))
print(per(5))
print(per(10))
# Traceback (most recent call last):
#   File "d:\workspace\python\test\test.py", line 9, in <module>
#     print(per(1))
#   File "d:\workspace\python\test\test.py", line 5, in per
#     total += num
# UnboundLocalError: local variable 'total' referenced before assignment
total = 0
nums = 0

def per(num: int) -> float:
    global total,nums
    total += num
    nums += 1
    return total/nums

print(per(1))
print(per(5))
print(per(10))
# 1.0
# 3.0
# 5.333333333333333
def getPer():
    numbers = []
    def per(num: int) -> float:
        numbers.append(num)
        return sum(numbers)/len(numbers)
    return per
per = getPer()
print(per(1))
print(per(5))
print(per(10))
# 1.0
# 3.0
# 5.333333333333333
print(per.__code__.co_varnames)
print(per.__code__.co_freevars)
# ('num',)
# ('numbers',)
def getPer():
    total = 0
    nums = 0

    def per(num: int) -> float:
        nonlocal total, nums
        total += num
        nums += 1
        return total/nums
    return per


per = getPer()
print(per(1))
print(per(5))
print(per(10))
# 1.0
# 3.0
# 5.333333333333333
print(per.__code__.co_varnames)
print(per.__code__.co_freevars)
# ('num',)
# ('nums', 'total')
from clock import clock


@clock
def fibonacci(n: int):
    if n <= 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(2))
print(fibonacci(5))
# [0.00000000s] fibonacci(2)->1
# 1
# [0.00000000s] fibonacci(2)->1
# [0.00000000s] fibonacci(1)->1
# [0.00000000s] fibonacci(3)->2
# [0.00000000s] fibonacci(2)->1
# [0.00100803s] fibonacci(4)->3
# [0.00000000s] fibonacci(2)->1
# [0.00000000s] fibonacci(1)->1
# [0.00098610s] fibonacci(3)->2
# [0.00199413s] fibonacci(5)->5
# 5
