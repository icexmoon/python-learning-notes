from vector_n import VectorN
v1 = VectorN([i for i in range(6)])
v2 = +v1
print(v1 is v2)
print(v1 == v2)
# False
# True
v3 = -v1
print(v3)
print(-v3 == v1)
# (-0.0, -1.0, -2.0, -3.0, -4.0, -5.0)
# True
v4 = VectorN(10 for i in range(6))
v5 = v4+v1
print(v5)
# (10.0, 11.0, 12.0, 13.0, 14.0, 15.0)
v6 = VectorN(10 for i in range(3))
print(v1+v6)
# (10.0, 11.0, 12.0, 3.0, 4.0, 5.0)
# print(v1+[1,2,3])
# (1.0, 3.0, 5.0, 3.0, 4.0, 5.0)
# print([1,2,3]+v1)
# Traceback (most recent call last):
#   File "D:\workspace\python\python-learning-notes\note30\test.py", line 20, in <module>
#     print(v1+[1,2,3])
# TypeError: unsupported operand type(s) for +: 'VectorN' and 'list'
print(10*v1)
# (0.0, 10.0, 20.0, 30.0, 40.0, 50.0)
print([1,2]==(1,2))
# False
l1 = [range(6)]
print(v1 == l1)
# False
from vector import Vector
v7 = VectorN([1,2])
v8 = Vector(1,2)
print(v7==v8)
# True
v1_alis = v1
v1+=VectorN(10 for i in range(6))
print(v1)
print(v1_alis)
print(v1 is v1_alis)
# (10.0, 11.0, 12.0, 13.0, 14.0, 15.0)
# (0.0, 1.0, 2.0, 3.0, 4.0, 5.0)
# False
from customer_list import CustomerList
c1 = CustomerList([1,2,3])
c1_alis = c1
c2 = CustomerList(10 for i in range(3))
c1 += c2
print(c1)
print(c1_alis)
print(c1 is c1_alis)
# [11, 12, 13]
# [11, 12, 13]
# True