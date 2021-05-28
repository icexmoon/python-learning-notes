from typing import Any


class TestClass:
    def __init__(self, default=None) -> None:
        self.default = default

    def __getattr__(self, name):
        setattr(self, name, self.default)
        return self.__dict__[name]

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

tc = TestClass()
tc.opt1 = 1
print(tc.opt2)
print(tc.__dict__)
# None
# {'default': None, 'opt1': 1, 'opt2': None}