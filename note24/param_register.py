registed = []


def register(reaRegist=True):
    def registerDecorator(func):
        if reaRegist:
            registed.append(func)
            print(str(func), "is registed")
        return func
    return registerDecorator


@register()
def test1():
    print('this is test1 function')


@register(False)
def test2():
    print('this is test2 function')


print("main function begin")
print(registed)
test1()
test2()
# <function test1 at 0x000001CB6F143B80> is registed
# main function begin
# [<function test1 at 0x000001CB6F143B80>]
# this is test1 function
# this is test2 function