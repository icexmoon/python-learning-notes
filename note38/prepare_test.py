import collections
class TestMetaClass(type):
    @classmethod
    def __prepare__(cls, name, bases):
        return collections.OrderedDict()

    def __init__(cls, name, bases, clsBody):
        super().__init__(name, bases, clsBody)
        for key, value in clsBody.items():
            if not callable(value):
                print("{}={}".format(key,value))
        

class TestClass(object,metaclass=TestMetaClass):
    attr1 = 1
    attr2 = 2
    def __init__(self) -> None:
        pass

tc = TestClass()
# __module__=__main__
# __qualname__=TestClass
# attr1=1
# attr2=2