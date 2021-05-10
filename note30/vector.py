import math
import array


class Vector():
    # double
    typeCode = 'd'
    # __slots__ = ("__x", "__y")

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        className = type(self).__name__
        return "{}({!r}, {!r})".format(className, *self)

    def __str__(self):
        return str(tuple(self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __bytes__(self):
        toArray = array.array(self.typeCode, self)
        return self.typeCode.encode('UTF-8')+bytes(toArray)

    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, format_spec):
        if format_spec.endswith('p'):
            r = abs(self)
            theta = self.angle()
            return "<{},{}>".format(r,theta)
        else:
            fmtX = format(self.x, format_spec)
            fmtY = format(self.y, format_spec)
            return "({},{})".format(fmtX, fmtY)

    @classmethod
    def fromBytes(cls, bytesVector):
        codeType = chr(bytesVector[0])
        arrayVector = array.array(codeType)
        arrayVector.frombytes(bytesVector[1:])
        return cls(*arrayVector)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)


if __name__ == '__main__':
    vector = Vector(3, 4)
    bytesVector = bytes(vector)
    vecotr2 = Vector.fromBytes(bytesVector)
    print(vecotr2)
    print(vector == vecotr2)
    # (3.0, 4.0)
    # True
