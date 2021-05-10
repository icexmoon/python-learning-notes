from collections import UserList
class CustomerList(UserList):
    def __iadd__(self, other):
        if not isinstance(other, CustomerList):
            return NotImplemented
        if len(self)!=len(other):
            raise TypeError("{!r} and {!r} need same length".format(self,other))
        for i in range(len(self)):
            self[i] += other[i]
        return self