def class_decorator(cls):
    def new_func(self):
        print("new_func() is called")
    cls.func_x = new_func
    return cls

@class_decorator
class TestClass:
    def func_x(self):
        print('func_x() is called')

class SubTestClass(TestClass):
    def func_x(self):
        print('SubTestClass.func_x() is called')

class SubTestClass2(TestClass):
    def func_x(self):
        super().func_x()

test = TestClass()
test.func_x()
test2 = SubTestClass()
test2.func_x()
test3 = SubTestClass2()
test3.func_x()
# new_func() is called
# SubTestClass.func_x() is called
# new_func() is called