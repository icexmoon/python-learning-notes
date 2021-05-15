import inspect
import random


def coroutineAverager():
    total = 0.0
    count = 0
    result = 0.0
    while True:
        try:
            newNumber = yield result
        except GeneratorExit:
            break
        total += newNumber
        count += 1
        result = total/count


avg = coroutineAverager()
next(avg)
numbers = [random.randint(1, 20) for i in range(5)]
countedNums = []
for i in numbers:
    result = avg.send(i)
    countedNums.append(i)
    print(countedNums, "average:", result)
# avg.close()
try:
    avg.throw(GeneratorExit)
except StopIteration:
    pass
print(inspect.getgeneratorstate(avg))
# [4] average: 4.0
# [4, 15] average: 9.5
# [4, 15, 14] average: 11.0
# [4, 15, 14, 7] average: 10.0
# [4, 15, 14, 7, 1] average: 8.2
# GEN_CLOSED
