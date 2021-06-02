import abc
from typing import ValuesView


class AttributeProxy:
    def __init__(self, name) -> None:
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class ValidatableAttr(abc.ABC, AttributeProxy):
    @abc.abstractmethod
    def validate(self, value):
        pass

    def __set__(self, instance, value):
        value = self.validate(value)
        super().__set__(instance, value)


class PositiveNumber(ValidatableAttr):
    def validate(self, value):
        if value > 0:
            return value
        else:
            raise ValueError('value must > 0')


class TextNotEmpty(ValidatableAttr):
    def validate(self, value):
        value = str(value).strip()
        if len(value) > 0:
            return value
        else:
            raise ValueError('text must not empty string')


class Order:
    quantity = PositiveNumber('quantity')
    price = PositiveNumber('price')
    des = TextNotEmpty('des')

    def __init__(self, quantity, price, des) -> None:
        self.quantity = quantity
        self.price = price
        self.des = des

    def total(self):
        return self.quantity*self.price


order = Order(1.5, 5, 'banana')
print(order.total())
print(vars(order))
order2 = Order(2, 3, '')
print(order2.total())
# 7.5
# {'quantity': 1.5, 'price': 5, 'des': 'banana'}
# Traceback (most recent call last):
#   File "D:\workspace\python\python-learning-notes\note37\test.py", line 60, in <module>
#     order2 = Order(2, 3, '')
#   File "D:\workspace\python\python-learning-notes\note37\test.py", line 51, in __init__
#     self.des = des
#   File "D:\workspace\python\python-learning-notes\note37\test.py", line 22, in __set__
#     value = self.validate(value)
#   File "D:\workspace\python\python-learning-notes\note37\test.py", line 40, in validate
#     raise ValueError('text must not empty string')
# ValueError: text must not empty string