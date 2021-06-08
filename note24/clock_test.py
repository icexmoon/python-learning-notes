from clock import clock


@clock
def fibonacci(n: int):
    if n <= 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(2))
print(fibonacci(5))
# [0.00000000s] fibonacci(2)->1
# 1
# [0.00000000s] fibonacci(2)->1
# [0.00000000s] fibonacci(1)->1
# [0.00000000s] fibonacci(3)->2
# [0.00000000s] fibonacci(2)->1
# [0.00100803s] fibonacci(4)->3
# [0.00000000s] fibonacci(2)->1
# [0.00000000s] fibonacci(1)->1
# [0.00098610s] fibonacci(3)->2
# [0.00199413s] fibonacci(5)->5
# 5