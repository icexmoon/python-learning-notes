class TestClass:
    def __init__(self) -> None:
        self.opt1 = 1
        self.opt2 = 2

    def __delattr__(self, name: str) -> None:
        value = getattr(self, name)
        super().__delattr__(name)
        newName = 'deled_'+str(name)
        setattr(self, newName, value)

tc = TestClass()
del tc.opt1
del tc.opt2
print(tc.__dict__)
# {'deled_opt1': 1, 'deled_opt2': 2}