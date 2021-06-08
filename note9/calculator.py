class Calculator():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        self.beforeRun("add")
        return self.a+self.b

    def beforeRun(self, operateName):
        print("calculator will operate ", operateName)


cal = Calculator(1, 2)
result = cal.add()
print(result)