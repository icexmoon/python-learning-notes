def throwExp():
    raise Exception()

try:
    throwExp()
except:
    print("catch a exception")
# catch a exception
try:
    a = 2/0
except ZeroDivisionError:
    print("catch a zero division exception")
# catch a zero division exception
try:
    a = 2/0
except ZeroDivisionError as e:
    print("catch a zero division exception")
    print(e)
# catch a zero division exception
# division by zero
try:
    a = 2/0
except Exception as e:
    print("catch a zero division exception")
    print(e)
# catch a zero division exception
# division by zero
from sys import exc_info
try:
    a = 2/0
except Exception:
    print("catch a zero division exception")
    print(exc_info())
# catch a zero division exception
# (<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero'), <traceback object at 0x00000210CB358A40>)