from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        '''这是一个抽象方法'''
        pass


class SubBase(Base):
    def fly(self):
        print("I can fly")


# base = Base() 会报错，因为抽象类不能实例化
base = SubBase()
base.fly()
# I can fly
