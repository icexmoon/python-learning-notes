class TestClass:
    def testMethod(self):
        pass

tc = TestClass()
print(tc.testMethod)
print(TestClass.testMethod)
print(TestClass.testMethod.__get__(tc))
print(TestClass.testMethod.__get__(None, TestClass))
print(tc.testMethod.__self__)
print(tc.testMethod.__func__)
# <bound method TestClass.testMethod of <__main__.TestClass object at 0x00000165D2446850>>
# <function TestClass.testMethod at 0x00000165D242D3A0>
# <bound method TestClass.testMethod of <__main__.TestClass object at 0x00000165D2446850>>
# <function TestClass.testMethod at 0x00000165D242D3A0>
# <__main__.TestClass object at 0x00000165D2446850>
# <function TestClass.testMethod at 0x00000165D242D3A0>