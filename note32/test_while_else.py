i = 1
while i <= 3:
    print("->{!s}".format(i))
    i += 1
else:
    print("else is excuted")
# ->1
# ->2
# ->3
# else is excuted
i = 1
while i <= 3:
    print("->{!s}".format(i))
    i += 1
    if i == 4:
        continue
else:
    print("else is excuted")
# ->1
# ->2
# ->3
# else is excuted
i = 1
while i <= 3:
    print("->{!s}".format(i))
    i += 1
    if i == 2:
        break
else:
    print("else is excuted")
# ->1
i = 1
try:
    while i <= 3:
        print("->{!s}".format(i))
        i += 1
        if i == 2:
            raise ZeroDivisionError
    else:
        print("else is excuted")
except ZeroDivisionError:
    pass
# ->1