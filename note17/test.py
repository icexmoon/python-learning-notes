people = ["jack chen", "brus lee"]
jackChen = people[0]
brusLee = people[1]

people = ["jack chen", "brus lee"]
jackChen, brusLee = people
print(jackChen, brusLee)
# jack chen brus lee
jackChen, brusLee = ["jack chen", "brus lee"]
print(jackChen, brusLee)
# jack chen brus lee
numbers = [i for i in range(1, 20, 2)]
print(numbers)
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
numbers = [i for i in range(1, 20, 2)]
print(numbers)
num1, num2, num3, *numOthers, numEnd = numbers
print(num1, num2, num3, numEnd)
print(numOthers)
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# 1 3 5 19
# [7, 9, 11, 13, 15, 17]
numbers = [i for i in range(1, 20, 2)]
print(numbers)
*_, last1, last2 = numbers
print(last1, last2)
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# 17 19
people = [["jack chen", 16, "actor"], ["brus Lee", "engineer"]]
for person in people:
    name, *info = person
    print("name is ", name, "person info is ", info)
# name is  jack chen person info is  [16, 'actor']
# name is  brus Lee person info is  ['engineer']
numbers1 = [1, 2, 3]
numbers2 = [7, 8, 9]
numbers3 = numbers1+numbers2
print(numbers3)
# [1, 2, 3, 7, 8, 9]
print('-'*10)
# ----------
numbers = [1, 2, 3]
print(numbers*3)
# [1, 2, 3, 1, 2, 3, 1, 2, 3]
numbers = [[]]*3
print(numbers)
numbers[0].append(1)
print(numbers)
# [[], [], []]
# [[1], [1], [1]]
numbers = [[] for i in range(0, 3)]
print(numbers)
numbers[0].append(1)
numbers[1].append(2)
numbers[2].append(3)
print(numbers)
# [[], [], []]
# [[1], [2], [3]]