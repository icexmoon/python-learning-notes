from collections import namedtuple
Student = namedtuple('Student', 'age name sex')
s1 = Student(15,'Han Meimei','female')
s2 = Student(20, 'Li Lei', 'male')
print(s1)
print(s2.name)
# Student(age=15, name='Han Meimei', sex='female')
# Li Lei