class OverrideAttr:
    def __init__(self, name) -> None:
        self.name = name
    def __get__(self, instance, owner):
        print('__get__ is called')
        return instance.__dict__[self.name]
class ProxyClass:
    overrideAttr = OverrideAttr('overrideAttr')

pc = ProxyClass()
# print(pc.overrideAttr)
# __get__ is called
# Traceback (most recent call last):
#   File "D:\workspace\python\python-learning-notes\note37\test.py", line 11, in <module>
#     print(pc.overrideAttr)
#   File "D:\workspace\python\python-learning-notes\note37\test.py", line 6, in __get__
#     return instance.__dict__[self.name]
# KeyError: 'overrideAttr'
pc.__dict__['overrideAttr'] = 1
print(pc.overrideAttr)
pc.overrideAttr = 2
# 1