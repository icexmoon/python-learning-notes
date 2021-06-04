class PositiveNumber:
    count = 0

    def __init__(self) -> None:
        clsName = self.__class__.__name__
        self.realName = "{}#{}".format(clsName, self.__class__.count)
        self.__class__.count += 1

    def __get__(self, instance, owner):
        return getattr(instance, self.realName)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.realName, value)
        else:
            raise ValueError('vlaue mast > 0')


class OrderMetaClass(type):
    def __init__(self, clsName, bases, clsBody):
        super().__init__(clsName, bases, clsBody)
        for key, value in clsBody.items():
            if isinstance(value, PositiveNumber):
                value.realName = "{}#{}".format(value.__class__.__name__, key)


class Order(metaclass=OrderMetaClass):
    quantity = PositiveNumber()
    price = PositiveNumber()

    def __init__(self, quantity, price) -> None:
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.quantity*self.price


class SubOrder(Order):
    pass


order = SubOrder(1.5, 5)
print(order.total())
print(vars(order))
# 7.5
# {'PositiveNumber#quantity': 1.5, 'PositiveNumber#price': 5}
