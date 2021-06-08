class sampleCls:
    @classmethod
    def classMethod(cls):
        print(cls)
        print("this is a class method")

    def objMethod(self):
        print(self)
        print("this is a object method")

a = sampleCls()
a.objMethod()
sampleCls.classMethod()
# <__main__.sampleCls object at 0x000001F963AF88E0>
# this is a object method
# <class '__main__.sampleCls'>
# this is a class method