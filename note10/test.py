class ListReader():
    def __init__(self, aList: list):
        self.list = aList

    def __enter__(self) -> list:
        print("will print a list:")
        return self.list

    def __exit__(self, expType, expVal, expTrace):
        print("end")


aList = [1, 2, 3, 4, 5, 6]
with ListReader(aList) as lr:
    print(lr)
# will print a list:
# [1, 2, 3, 4, 5, 6]
# end