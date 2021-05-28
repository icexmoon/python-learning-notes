from collections.abc import Iterable
class TestClass:
    def __init__(self) -> None:
        self.opt1 = 1
        self.opt2 = 2
    
    def __dir__(self) -> Iterable[str]:
        res = list(super().__dir__())
        res.append('del_XXX')
        return res

tc = TestClass()
print(dir(tc))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', 
# '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'del_XXX', 'opt1', 'opt2']