a = {"name": "jack chen",
     "age": 16}
a["career"] = "actor"
print(a)
# {'name': 'jack chen', 'age': 16, 'career': 'actor'}
a = {"name": "jack chen",
     "age": 16}
a["career"] = "actor"
del a["age"]
print(a)
# {'name': 'jack chen', 'career': 'actor'}
a = {"name": "jack chen",
     "age": 16}
a["career"] = "actor"
for column in a:
    print(column)
# name
# age
# career
a = {"name": "jack chen",
     "age": 16,
     "career": "actor"}
for key, val in a.items():
    print(key, ": ", val)
# name :  jack chen
# age :  16
# career :  actor
a = {"name": "jack chen",
     "age": 16,
     "career": "actor"}
for key, val in sorted(a.items()):
    print(key, ": ", val)
# age :  16
# career :  actor
# name :  jack chen
a = {"name": "jack chen",
     "age": 16,
     "career": "actor"}
aSort = ["name", "career", "age"]
for key in aSort:
    print(key, ": ", a[key])
# name :  jack chen
# career :  actor
# age :  16
a = list("Hellow World!")
count = {}
for char in a:
    if not char in count:
        count[char] = 0
    count[char] += 1
print(count)
# {'H': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1, '!': 1}
a = list("Hellow World!")
count = {}
for char in a:
    count.setdefault(char, 0)
    count[char] += 1
print(count)
# {'H': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1, '!': 1}