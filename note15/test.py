string = "this is a test String"
strList = []
for char in string:
    strList.append(char)
print(strList)
# ['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 't', 'e', 's', 't', ' ', 'S', 't', 'r', 'i', 'n', 'g']
string = "this is a test String"
strList = [char for char in string]
print(strList)
# ['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 't', 'e', 's', 't', ' ', 'S', 't', 'r', 'i', 'n', 'g']
a = (1, 2, 3, 4, 5)
b = []
for i in a:
    if i % 2 == 0:
        b.append(i*3)
print(b)
# [6, 12]
a = (1, 2, 3, 4, 5)
b = [num*3 for num in a if num % 2 == 0]
print(b)
# [6, 12]
import pprint
peopleList = [["jack chen", 16], ["brus lee", 20]]
peopleDict = {}
for person in peopleList:
    peopleDict[person[0]] = person[1]
pprint.pprint(peopleDict)
# {'brus lee': 20, 'jack chen': 16}
import pprint
peopleList = [["jack chen", 16], ["brus lee", 20]]
peopleDict = {person[0]: person[1] for person in peopleList}
pprint.pprint(peopleDict)
# {'brus lee': 20, 'jack chen': 16}
import pprint
peopleList = [["jack chen", 16], ["brus lee", 20]]
peopleSet = set()
for person in peopleList:
    peopleSet.add(person[0])
pprint.pprint(peopleSet)
# {'brus lee', 'jack chen'}
import pprint
peopleList = [["jack chen", 16], ["brus lee", 20]]
peopleSet = {person[0] for person in peopleList}
pprint.pprint(peopleSet)
# {'jack chen', 'brus lee'}