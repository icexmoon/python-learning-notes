string = "Hellow Wolrd"
a = list(string)
print(a)
# ['H', 'e', 'l', 'l', 'o', 'w', ' ', 'W', 'o', 'l', 'r', 'd']
a=list(range(6))
print(a)
# [0, 1, 2, 3, 4, 5]
a = list(range(10, 0, -1))
print(a)
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
a = list(range(5, 0, -1))
for num in a :
    print(num)
# 5
# 4
# 3
# 2
# 1
a = list(range(5, 0, -1))
a.append(99)
print(a)
# [5, 4, 3, 2, 1, 99]
a = list(range(5, 0, -1))
a.insert(0,99)
print(a)
# [99, 5, 4, 3, 2, 1]
a = list(range(5, 0, -1))
a.extend([98,99])
print(a)
# [5, 4, 3, 2, 1, 98, 99]
a = list(range(5, 0, -1))
a.pop()
print(a)
# [5, 4, 3, 2]
a = list(range(5, 0, -1))
a.pop(1)
print(a)
# [5, 3, 2, 1]
a = list(range(5, 0, -1))
index = 0
for val in a:
    if index == 1 or index == 2:
        a.pop(index)
    index += 1
print(a)
# [5, 3, 1]
a = list(range(5, 0, -1))
index = 0
for val in a:
    if index == 1 or index == 2:
        a[index] = None
    index += 1
print(a)
# [5, None, None, 2, 1]
a = list(range(5, 0, -1))
index = 0
b = []
for val in a:
    if not(index == 1 or index == 2):
        b.append(val)
    index += 1
a = b
print(a)
# [5, 2, 1]
a = list(range(5, 0, -1))
a.remove(1)
print(a)
# [5, 4, 3, 2]
a = list(range(5, 0, -1))
a[1] = 99
print(a)
# [5, 99, 3, 2, 1]
a = list(range(10, 0, -1))
b = a[1:5:1]
print(a)
print(b)
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# [9, 8, 7, 6]
a = list(range(10, 0, -1))
b = a[-1:5:-1]
print(a)
print(b)
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# [1, 2, 3, 4]