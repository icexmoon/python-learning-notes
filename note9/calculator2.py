class Calculator():
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def add(self):
        self.__beforeRun("add")
        return self.__a+self.__b

    def __beforeRun(self, operateName):
        print("calculator will operate ", operateName)


cal = Calculator(1, 2)
result = cal.add()
print(result)
# print(cal.__a)
# cal.__beforeRun("see")