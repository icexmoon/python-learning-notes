class TestClass:
    def __init__(self) -> None:
        pass

    def __setattr__(self, name, value):
        newVlue = 'new_'+str(value)
        super().__setattr__(name, newVlue)

tc = TestClass()
tc.opt1 = 1
print(tc.opt1)
# new_1