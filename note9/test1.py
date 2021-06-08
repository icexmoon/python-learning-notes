class Test():
    def __init__(self, a: int = 0):
        self.a = a

    def print(self) -> None:
        print(self.a)


test = Test()
test2 = Test(2)
test.print()
test2.print()
# 0
# 2