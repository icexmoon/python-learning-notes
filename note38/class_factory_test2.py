def named_tuple_factory(clsName, fields):
    try:
        fields = fields.replace(',', ' ').split(' ')
    except AttributeError:
        pass
    clsBody = {}
    clsBody['__slots__'] = tuple(fields)

    def __init__(self, *args, **kwArgs):
        if args:
            for key, value in zip(fields, args):
                setattr(self, key, value)
        if kwArgs:
            for key, value in kwArgs.items():
                setattr(self, key, value)

    def __str__(self):
        fieldsStr = ",".join("{}={!s}".format(key, getattr(self, key))
                             for key in self.__slots__)
        return "{}({})".format(clsName, fieldsStr)
    clsBody['__init__'] = __init__
    clsBody['__str__'] = __str__
    return type(clsName, (object,), clsBody)


Student = named_tuple_factory('Student', 'name,age,sex')
s1 = Student('Han Meimei', 16, 'female')
s2 = Student('Li Lei', 20, 'male')
print(s1)
print(s2.name)
Student = named_tuple_factory('Student', 'name age sex')
s1 = Student('Han Meimei', 16, 'female')
print(s1)
Student = named_tuple_factory('Student', ('name', 'age', 'sex'))
s1 = Student(name='Han Meimei', age=16, sex='female')
print(s1)
# Student(name=Han Meimei,age=16,sex=female)
# Li Lei
# Student(name=Han Meimei,age=16,sex=female)
# Student(name=Han Meimei,age=16,sex=female)
