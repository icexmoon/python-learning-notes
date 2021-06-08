# from clock import clockWithParam
from clock import clock
from functools import lru_cache

@lru_cache()
@clock
def fibonacci(n: int):
    if n <= 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

# print(fibonacci(2))
# print(fibonacci(5))
print(fibonacci.__name__)
# clocked