a = 1
b = 1
print(id(1))
print(id(a))
print(id(b))
help(id)
# 2404179011888
# 2404179011888
# 2404179011888
# Help on built-in function id in module builtins:

# id(obj, /)
#     Return the identity of an object.

#     This is guaranteed to be unique among simultaneously existing objects.
#     (CPython uses the object's memory address.)
a = 1
b = a
b = 2
print(a)
print(b)
a = [1, 2, 3]
b = a
b[0] = 2
print(a)
print(b)
# 1
# 2
# [2, 2, 3]
# [2, 2, 3]
