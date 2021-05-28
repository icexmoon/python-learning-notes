class TestClass:
    def __init__(self) -> None:
        self.__opt1 = 1

    @property
    def opt1(self):
        '''this is a property doc'''
        return self.__opt1

help(TestClass.opt1)
# Help on property:

#     this is a property doc