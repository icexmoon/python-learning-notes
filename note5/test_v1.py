#test.py
def test():
    print("this is a module test")
a=test
a()
print(dir())
print(__name__)
# this is a module test
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'test']        
# __main__