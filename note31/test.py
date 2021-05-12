from collections import abc
from sentence import Sentence
s = Sentence("Today is a good day!")
for word in s:
    print(word)
sIter = iter(s)
print(sIter)
for word in sIter:
    print(word)
# Today
# is
# a
# good
# day
# <iterator object at 0x000002870BB7B4C0>
# Today
# is
# a
# good
# day
print(isinstance(s, abc.Iterable))
print(issubclass(Sentence, abc.Iterable))
# False
# False

sIter = iter(s)
already = []
while True:
    print("{!s}^{!s}".format(already, sIter))
    try:
        item = next(sIter)
    except StopIteration:
        break
    already.append(item)
# []^<iterator object at 0x000001D67CD6B4F0>
# ['Today']^<iterator object at 0x000001D67CD6B4F0>
# ['Today', 'is']^<iterator object at 0x000001D67CD6B4F0>
# ['Today', 'is', 'a']^<iterator object at 0x000001D67CD6B4F0>
# ['Today', 'is', 'a', 'good']^<iterator object at 0x000001D67CD6B4F0>
# ['Today', 'is', 'a', 'good', 'day']^<iterator object at 0x000001D67CD6B4F0>
from sentence_v2 import SentenceV2,StenceIterator
s = SentenceV2("Today is a good day!")
sIter = iter(s)
already = []
while True:
    print("{!s}^{!s}".format(already, sIter))
    try:
        item = next(sIter)
    except StopIteration:
        break
    already.append(item)
print(issubclass(SentenceV2, abc.Iterable))
print(isinstance(s, abc.Iterable))
print(issubclass(StenceIterator, abc.Iterator))
print(isinstance(sIter, abc.Iterator))
# []^<sentence_v2.StenceIterator object at 0x000002200527E550>
# ['Today']^<sentence_v2.StenceIterator object at 0x000002200527E550>
# ['Today', 'is']^<sentence_v2.StenceIterator object at 0x000002200527E550>
# ['Today', 'is', 'a']^<sentence_v2.StenceIterator object at 0x000002200527E550>
# ['Today', 'is', 'a', 'good']^<sentence_v2.StenceIterator object at 0x000002200527E550>
# ['Today', 'is', 'a', 'good', 'day']^<sentence_v2.StenceIterator object at 0x000002200527E550>
# True
# True
# True
# True
def genTest():
    print('before 1')
    yield 1
    print('before 2')
    yield 2
    print('before 3')
    yield 3
    print('end')

gen = genTest()
print(gen)
print(isinstance(gen, abc.Iterator))
while True:
    try:
        item = next(gen)
    except StopIteration:
        break
    print('get:',item)
# <generator object genTest at 0x000001CFCC21B120>
# True
# before 1
# get: 1
# before 2
# get: 2
# before 3
# get: 3
# end
# Traceback (most recent call last):
#   File "D:\workspace\python\python-learning-notes\note31\test.py", line 79, in <module>
#     item = next(gen)
# StopIteration
from sentence_v4 import SentenceV4
s = SentenceV4("Today is a good day!")
for word in s:
    print(word)
# Today
# is
# a
# good
# day
l = [['a','b','c'],[1,2,3]]
def genTest2(l):
    for i in l:
        for j in i:
            yield j
for i in genTest2(l):
    print(i)
# a
# b
# c
# 1
# 2
# 3
l = [['a','b','c'],[1,2,3]]
def genTest2(l):
    for i in l:
        yield from i
for i in genTest2(l):
    print(i)
# a
# b
# c
# 1
# 2
# 3
from sentence_v5 import SentenceV5
s = SentenceV5("Today is a good day!")
for word in s:
    print(word)
# Today
# is
# a
# good
# day
import itertools
data = [i for i in range(6)]
selectors = [True, False, False, True]
for result in itertools.compress(data,selectors):
    print(result)
# 0
# 3
numbers = [i for i in range(10)]
for result in itertools.dropwhile(lambda x:x<5,numbers):
    print(result)
# 5
# 6
# 7
# 8
# 9
numbers = [i for i in range(10)]
for result in filter(lambda x: x%2==0,numbers):
    print(result)
# 0
# 2
# 4
# 6
# 8
for result in itertools.filterfalse(lambda x: x%2==0,range(10)):
    print(result)
# 1
# 3
# 5
# 7
# 9
numbers = [number*2 for number in range(10)]
for result in itertools.islice(numbers,5):
    print(result)
# 0
# 2
# 4
# 6
# 8
example = [1,2,3,4,5,4,3,2,1]
for result in itertools.takewhile(lambda x: x<=3,example):
    print(result)
# 1
# 2
# 3
import operator
for result in itertools.accumulate(range(1,11),operator.mul,initial=1):
    print(result)
# 1
# 1
# 2
# 6
# 24
# 120
# 720
# 5040
# 40320
# 362880
# 3628800
enumSuites = {}
for value,suit in enumerate(['方块','梅花','红桃','黑桃'],start=1):
    print("花色：{},值：{}".format(suit,value))
    enumSuites[value] = suit
newSuit = 3
newSuitName = enumSuites[newSuit]
print(newSuitName)
# 花色：方块,值：1
# 花色：梅花,值：2
# 花色：红桃,值：3
# 花色：黑桃,值：4
# 红桃
for result in map(operator.add,range(10),range(6)):
    print(result)
# 0
# 2
# 4
# 6
# 8
# 10
example = [(i,i) for i in range(6)]
for result in itertools.starmap(operator.add, example):
    print(result)
# 0
# 2
# 4
# 6
# 8
# 10
for result in itertools.chain('abc',range(6)):
    print(result)
# a
# b
# c
# 0
# 1
# 2
# 3
# 4
# 5
example = enumerate('abcde',start=1)
for result in itertools.chain.from_iterable(example):
    print(result)
# 1
# a
# 2
# b
# 3
# c
# 4
# d
# 5
# e
suites = ['红桃','黑桃','方块','梅花']
numbers = [i for i in range(2,11)]+['J','Q','K','A']
for result in itertools.product(suites,numbers):
    print(result)
# ('红桃', 2)
# ('红桃', 3)
# ('红桃', 4)
# ('红桃', 5)
# ('红桃', 6)
# ('红桃', 7)
# ('红桃', 8)
# ('红桃', 9)
# ('红桃', 10)
# ('红桃', 'J')
# ('红桃', 'Q')
# ('红桃', 'K')
# ('红桃', 'A')
# ('黑桃', 2)
# ('黑桃', 3)
# ('黑桃', 4)
# ('黑桃', 5)
# ('黑桃', 6)
# ('黑桃', 7)
# ('黑桃', 8)
# ('黑桃', 9)
# ('黑桃', 10)
# ('黑桃', 'J')
# ('黑桃', 'Q')
# ('黑桃', 'K')
# ('黑桃', 'A')
# ('方块', 2)
# ('方块', 3)
# ('方块', 4)
# ('方块', 5)
# ('方块', 6)
# ('方块', 7)
# ('方块', 8)
# ('方块', 9)
# ('方块', 10)
# ('方块', 'J')
# ('方块', 'Q')
# ('方块', 'K')
# ('方块', 'A')
# ('梅花', 2)
# ('梅花', 3)
# ('梅花', 4)
# ('梅花', 5)
# ('梅花', 6)
# ('梅花', 7)
# ('梅花', 8)
# ('梅花', 9)
# ('梅花', 10)
# ('梅花', 'J')
# ('梅花', 'Q')
# ('梅花', 'K')
# ('梅花', 'A')
suites = ['红桃','黑桃','方块','梅花']
for result in itertools.product(suites, repeat=2):
    print(result)
# ('红桃', '红桃')
# ('红桃', '黑桃')
# ('红桃', '方块')
# ('红桃', '梅花')
# ('黑桃', '红桃')
# ('黑桃', '黑桃')
# ('黑桃', '方块')
# ('黑桃', '梅花')
# ('方块', '红桃')
# ('方块', '黑桃')
# ('方块', '方块')
# ('方块', '梅花')
# ('梅花', '红桃')
# ('梅花', '黑桃')
# ('梅花', '方块')
# ('梅花', '梅花')
suites = ['红桃','黑桃','方块','梅花']
for result in itertools.combinations(suites,2):
    print(result)
# ('红桃', '黑桃')
# ('红桃', '方块')
# ('红桃', '梅花')
# ('黑桃', '方块')
# ('黑桃', '梅花')
# ('方块', '梅花')
print('='*10)
suites = ['红桃','黑桃','方块','梅花']
for result in itertools.combinations_with_replacement(suites,2):
    print(result)
# ==========
# ('红桃', '红桃')
# ('红桃', '黑桃')
# ('红桃', '方块')
# ('红桃', '梅花')
# ('黑桃', '黑桃')
# ('黑桃', '方块')
# ('黑桃', '梅花')
# ('方块', '方块')
# ('方块', '梅花')
# ('梅花', '梅花')
print('='*15)
suites = ['红桃','黑桃','方块','梅花']
for result in itertools.permutations(suites,2):
    print(result)
# ===============
# ('红桃', '黑桃')
# ('红桃', '方块')
# ('红桃', '梅花')
# ('黑桃', '红桃')
# ('黑桃', '方块')
# ('黑桃', '梅花')
# ('方块', '红桃')
# ('方块', '黑桃')
# ('方块', '梅花')
# ('梅花', '红桃')
# ('梅花', '黑桃')
# ('梅花', '方块')
for result in itertools.takewhile(lambda x:x<10, itertools.count(0,1.5)):
    print(result)
# 0
# 1.5
# 3.0
# 4.5
# 6.0
# 7.5
# 9.0
for result in itertools.islice(itertools.cycle("ABC"),10):
    print(result)
# A
# B
# C
# A
# B
# C
# A
# B
# C
# A
for result in map(operator.add,range(1,11),itertools.repeat(10)):
    print(result,end=' ')
print()
# 11 12 13 14 15 16 17 18 19 20
example = ['aaa','bbb','cccccc','dd','eee','ffffff']
example.sort(key=len)
for num,grouper in itertools.groupby(example,key=len):
    print("num:{},countents:".format(num),end='')
    for grouperItem in grouper:
        print(grouperItem,end=' ')
    print()
# num:2,countents:dd
# num:3,countents:aaa bbb eee
# num:6,countents:cccccc ffffff
iter1,iter2 = itertools.tee(range(10),2)
for num in iter1:
    print(num,end=' ')
print()
for num in iter2:
    print(num, end=' ')
print()
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
def showIteratorRemains(iterator):
    for item in  iterator:
        print(item,end=' ')
    print()
example = [1,2,3,0,0,1,5,0,3]
expIterator = iter(example)
print(all(expIterator))
showIteratorRemains(expIterator)
# False
# 0 1 5 0 3
import random
def roll():
    return random.randint(1,6)
rollIterator = iter(roll,6)
for result in rollIterator:
    print(result,end=' ')
print()
# 1 5 1 2 2 5 4 2
