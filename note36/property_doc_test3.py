class TestClass:
    def __init__(self) -> None:
        self.__opt1 = 1

    def get_opt1(self):
        return self.__opt1
    opt1 = property(fget=get_opt1,doc='this is a property doc')

help(TestClass.opt1)
# Help on property:

#     this is a property doc