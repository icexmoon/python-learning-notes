print('imported_test.py start')
class TestClass():
    print("TestClass body")
    def test(self):
        print("TestClass.test() body")
print('imported_test.py end')
if __name__ == '__main__':
    test = TestClass()
    test.test()