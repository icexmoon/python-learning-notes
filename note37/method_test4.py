class CachedAttr:
    def __init__(self, name, func) -> None:
        self.name = name
        self.func = func

    def __get__(self, instance, owner):
        try:
            return instance.__dict__[self.name]
        except KeyError:
            result = self.func()
            instance.__dict__[self.name] = result
            return result

import time
def longRunFunction():
    time.sleep(3)
    return "this is a long run result"

class TestClass:
    cachedAttr = CachedAttr('cachedAttr', longRunFunction)

tc = TestClass()
print(tc.cachedAttr)
print(tc.cachedAttr)
# this is a long run result
# this is a long run result