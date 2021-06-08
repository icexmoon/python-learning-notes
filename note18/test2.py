class A:
    def __init__(self):
        print("A.__init__()")

class B(A):
    def __init__(self):
        super().__init__()
        print("B.__init__()")

class C(A):
    def __init__(self):
        super().__init__()
        print("C.__init__()")

class D(B,C):
    def __init__(self):
        super().__init__()
        print("D.__init__()")

d = D()
print(D.__mro__)
# A.__init__()
# C.__init__()
# B.__init__()
# D.__init__()
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)