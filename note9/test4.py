class Test():
    def __init__(self, a: int = 0):
        self.a = a

    def print(self) -> None:
        print(self.a)

    def __repr__(self) -> str:
        return "this is a Test object,a:"+str(self.a)


test = Test()
test2 = Test(2)
print(test)
print(test2)
# this is a Test object,a:0
# this is a Test object,a:2