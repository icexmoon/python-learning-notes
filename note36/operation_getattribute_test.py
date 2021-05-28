from typing import Any


class TestClass:
    def __init__(self) -> None:
        self.opt1 = 1
        self.opt2 = 2

    def __getattribute__(self, name: str) -> Any:
        try:
            attr = super().__getattribute__(name)
        except AttributeError:
            setattr(self, name, 1)
            return super().__getattribute__(name)
        else:
            return attr

tc = TestClass()
print(tc.opt2)
print(tc.opt3)
# 2
# 1