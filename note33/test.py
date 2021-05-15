import pprint
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


def dealDataCoroutine(result, kind):
    result[kind] = yield from coroutineAverager()


data = {}
data["boy_height"] = [random.randint(160, 195) for i in range(10)]
data["girl_height"] = [random.randint(150, 185) for i in range(10)]
data["boy_weight"] = [random.randint(60, 100) for i in range(10)]
data["girl_weight"] = [random.randint(40, 80) for i in range(10)]
result = {}
for kind, kindData in data.items():
    ddc = dealDataCoroutine(result, kind)
    next(ddc)
    for item in kindData:
        ddc.send(item)
    try:
        ddc.send(None)
    except StopIteration:
        pass
pprint.pprint(data)
print(result)
# {'boy_height': [189, 192, 174, 163, 160, 171, 173, 170, 194, 186],
#  'boy_weight': [79, 78, 76, 98, 86, 81, 78, 68, 97, 68],
#  'girl_height': [165, 170, 167, 169, 174, 177, 161, 154, 177, 167],
#  'girl_weight': [51, 52, 65, 46, 78, 71, 75, 63, 58, 65]}
# {'boy_height': 177.2, 'girl_height': 168.1, 'boy_weight': 80.9, 'girl_weight': 62.4}
