class Test():
    def __init__(self, a: int = 0):
        self.a = a

    def print(self) -> None:
        print(self.a)


test = Test()
test2 = Test(2)
Test.print(test)
Test.print(test2)
# 0
# 2