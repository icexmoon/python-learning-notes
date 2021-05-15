import inspect
import random


def coroutineAverager():
    total = 0.0
    count = 0
    result = 0.0
    while True:
        newNumber = yield
        if newNumber is None:
            break
        total += newNumber
        count += 1
        result = total/count
    return result


avg = coroutineAverager()
next(avg)
numbers = [random.randint(1, 20) for i in range(5)]
for i in numbers:
    avg.send(i)
try:
    avg.send(None)
except StopIteration as e:
    print(numbers)
    print("avg:", e.value)
# [3, 18, 10, 9, 13]
# avg: 10.6
