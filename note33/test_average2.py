import inspect
import random


def coroutineAverager():
    total = 0.0
    count = 0
    result = 0.0
    while True:
        newNumber = yield result
        if newNumber is None:
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
try:
    avg.send(None)
except StopIteration:
    pass
# [13] average: 13.0
# [13, 8] average: 10.5
# [13, 8, 17] average: 12.666666666666666
# [13, 8, 17, 18] average: 14.0
# [13, 8, 17, 18, 5] average: 12.2