def tryDetectFunc():
    pass
def afterTryFunc():
    1/0
try:
    tryDetectFunc()
    afterTryFunc()
except Exception:
    pass

try:
    tryDetectFunc()
except Exception:
    pass
else:
    afterTryFunc()
# Traceback (most recent call last):
#   File "D:\workspace\python\python-learning-notes\note32\test.py", line 16, in <module>
#     afterTryFunc()
#   File "D:\workspace\python\python-learning-notes\note32\test.py", line 4, in afterTryFunc
#     1/0
# ZeroDivisionError: division by zero
