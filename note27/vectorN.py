import array
import numbers
import functools
import operator
import math
import itertools
import reprlib


class VectorN():
    typeCode = 'd'
    attrStr = "xyzt"

    def __init__(self, iterable):
        self.__contents = array.array(self.typeCode, iterable)

    def __iter__(self):
        return iter(self.contents)

    def __repr__(self):
        cls = type(self)
        clsName = cls.__name__
        if len(self.contents) == 0:
            return "{}()".format(clsName)
        string = reprlib.repr(self.contents)
        numbersStr = string[string.find('[')+1:-2]
        return "{}({})".format(clsName, numbersStr)

    def __str__(self):
        if len(self.contents) == 0:
            return "()"
        string = str(self.contents)
        numbersStr = string[string.find('[')+1:-2]
        return "({})".format(numbersStr)

    def __eq__(self, other):
        return len(self) != len(other) and all(num1 == num2 for num1,num2 in zip(self, other))

    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))

    def __bool__(self):
        return abs(self) != 0

    def __bytes__(self):
        return self.typeCode.encode('UTF-8')+bytes(self.contents)

    @classmethod
    def fromBytes(cls, bytesVectorN):
        typeCode = chr(bytesVectorN[0])
        arrayVectorN = array.array(typeCode)
        arrayVectorN.frombytes(bytesVectorN[1:])
        return cls(arrayVectorN)

    @property
    def contents(self):
        return self.__contents

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, numbers.Integral):
            return self.contents[index]
        elif isinstance(index, slice):
            # start,stop,step = index.indices(len(self))
            # subArray = self.contents[start:stop:step]
            subArray = self.contents[index]
            return cls(subArray)
        elif isinstance(index, tuple):
            raise TypeError(
                "list indices must be integers or slices, not tuple")
        else:
            raise TypeError("list indices must be integers or slices")

    def __len__(self):
        return len(self.contents)

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            index = cls.attrStr.find(name)
            if 0 <= index < len(self):
                return self.contents[index]
        raise IndexError("list index out of range")

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            msg = ""
            if name in cls.attrStr:
                msg = "readonly attribute {}".format(name)
            else:
                pass
            raise AttributeError(msg)
        super().__setattr__(name, value)

    def __hash__(self):
        hashes = [hash(num) for num in self.contents]
        return functools.reduce(operator.xor, hashes, 0)

    def angle(self, n):
        r = math.sqrt(sum(x*x for x in self[n:]))
        a = math.atan2(r, self[n-1])
        if (n == len(self)-1) and (self[-1]<0):
            return math.pi * 2 -a
        else:
            return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, format_spec):
        if format_spec.endswith('h'):
            format_spec = format_spec[:-1]
            coords = itertools.chain([abs(self)],self.angles())
            outer_fmt = "<{}>"
        else:
            coords = self
            outer_fmt = "({})"
        components = (format(c, format_spec) for c in coords)
        return outer_fmt.format(','.join(components))