iterator = range(1,4)
for i in iterator:
    print("->{!s}".format(i))
else:
    print("else block is called")
# ->1
# ->2
# ->3
# else block is called
iterator = range(1,4)
for i in iterator:
    print("->{!s}".format(i))
    if i == 3:
        break
else:
    print("else block is called")
# ->1
# ->2
# ->3
iterator = range(1,4)
for i in iterator:
    print("->{!s}".format(i))
    if i == 3:
        continue
else:
    print("else block is called")
# ->1
# ->2
# ->3
# else block is called
try:
    iterator = range(1,4)
    for i in iterator:
        print("->{!s}".format(i))
        if i == 3:
            raise ZeroDivisionError
    else:
        print("else block is called")
except ZeroDivisionError:
    pass
# ->1
# ->2
# ->3
