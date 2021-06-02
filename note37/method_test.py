class TestClass:
    def testMethod(self):
        pass

tc = TestClass()
print(tc.testMethod)
print(TestClass.testMethod)
# <bound method TestClass.testMethod of <__main__.TestClass object at 0x0000021954AC9310>>
# <function TestClass.testMethod at 0x0000021954AAD5E0>