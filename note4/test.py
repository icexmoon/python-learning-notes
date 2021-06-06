def hellowWorld():
    print("hellow world!")
hellowWorld()
# hellow world!
def showStr(string):
    print(string)


showStr("hellow world!")
# hellow world!
def showPerson(name, age):
    print("name: ", name)
    print("age:", age)


showPerson(age=16, name="Jack Lee")
# name:  Jack Lee
# age: 16
def doubleTuple(oneTuple):
    oneTuple = oneTuple*2
    print("after double: ", oneTuple)


oneTuple = ("a", "b", "c")
doubleTuple(oneTuple)
print(oneTuple)
# after double:  ('a', 'b', 'c', 'a', 'b', 'c')
# ('a', 'b', 'c')
def doubleList(oneList):
    oneList = oneList*2
    print("after double: ", oneList)


oneList = ["a", "b", "c"]
doubleList(oneList)
print(oneList)
# after double:  ['a', 'b', 'c', 'a', 'b', 'c']
# ['a', 'b', 'c']
def changeList(oneList):
    oneList.pop()
    print("after pop: ", oneList)


oneList = ["a", "b", "c"]
changeList(oneList)
print(oneList)
# after pop:  ['a', 'b']
# ['a', 'b']
def showPerson(name, age=16):
    print("name: ", name)
    print("age:", age)


showPerson("Jack Lee")
# name:  Jack Lee
# age: 16
def showPerson(name, age=16):
    """show a person information"""
    print("name: ", name)
    print("age:", age)


# showPerson("Jack Lee")
help(showPerson)
# Help on function showPerson in module __main__:

# showPerson(name, age=16)
#     show a person information
def showPerson(name: str, age: int = 16) -> None:
    """show a person information"""
    print("name: ", name)
    print("age:", age)


# showPerson("Jack Lee")
help(showPerson)
# Help on function showPerson in module __main__:

# showPerson(name: str, age: int = 16) -> None
#     show a person information