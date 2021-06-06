#test.py
import test2
def test():
    print("this is a module test")
a=test
a()
print(dir())
print(__name__)
test2.test2Function()
# this is module test2
# this is test2 module name:test2
# this is a module test
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'test', 'test2']
# __main__
# this is a function in module test2