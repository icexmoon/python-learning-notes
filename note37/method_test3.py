class TestClass:
    def testMethod(self):
        pass

tc = TestClass()
print(tc.testMethod)
tc.testMethod = 1
print(tc.testMethod)
# <bound method TestClass.testMethod of <__main__.TestClass object at 0x000001B2CBB68820>>
# 1