from param_clock import clockWithParam
from functools import lru_cache

@lru_cache()
@clockWithParam('{name}({argStr}) [{times:0.8f}]')
def fibonacci(n: int):
    if n <= 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(2))
print(fibonacci(5))
# fibonacci(2) [0.00000000]
# 1
# fibonacci(1) [0.00000000]
# fibonacci(3) [0.00000000]
# fibonacci(4) [0.00099969]
# fibonacci(5) [0.00099969]
# 5