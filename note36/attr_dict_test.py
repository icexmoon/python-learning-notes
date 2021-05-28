class TestClass:
    def __init__(self) -> None:
        pass


tc = TestClass()
print(tc.__dict__)
tc.newOpt = 'new'
print(tc.__dict__)
newOpts = {'opt1': 1, 'opt2': 2, 'opt3': 3}
tc.__dict__.update(newOpts)
print(tc.__dict__)
print(tc.newOpt)
print(tc.opt1)
print(tc.opt2)
print(tc.opt3)
# {}
# {'newOpt': 'new'}
# {'newOpt': 'new', 'opt1': 1, 'opt2': 2, 'opt3': 3}
# new
# 1
# 2
# 3
