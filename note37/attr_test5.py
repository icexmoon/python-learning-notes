class OverrideAttr:
    def __init__(self, name) -> None:
        self.name = name
    def __set__(self, instance, value):
        print('__set__ is called')
        instance.__dict__[self.name] = value
class ProxyClass:
    overrideAttr = OverrideAttr('overrideAttr')

pc = ProxyClass()
print(pc.overrideAttr)
pc.__dict__['overrideAttr'] = 1
print(pc.overrideAttr)
pc.overrideAttr = 2
# <__main__.OverrideAttr object at 0x000002206F9D8100>
# 1
# __set__ is called