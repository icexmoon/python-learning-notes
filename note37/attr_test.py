class PositiveNumber:
    def __init__(self, name) -> None:
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.name] = value
        else:
            raise ValueError('vlaue mast > 0')


class Order:
    quantity = PositiveNumber('quantity')
    price = PositiveNumber('price')

    def __init__(self, quantity, price) -> None:
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.quantity*self.price


order = Order(1.5, 5)
print(order.total())
order2 = Order(0, 3)
print(order2.total())
# 7.5
# Traceback (most recent call last):
#   File "D:\workspace\python\python-learning-notes\note37\test.py", line 29, in <module>
#     order2 = Order(0, 3)
#   File "D:\workspace\python\python-learning-notes\note37\test.py", line 20, in __init__
#     self.quantity = quantity
#   File "D:\workspace\python\python-learning-notes\note37\test.py", line 12, in __set__
#     raise ValueError('vlaue mast > 0')
# ValueError: vlaue mast > 0