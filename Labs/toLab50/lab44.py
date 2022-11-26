import functools
import time


@functools.lru_cache()
def fib_hard(n):

    if n < 2:
        result = n
    else:
        result = fib_hard(n-1) + fib_hard(n-2)

    return result


def fib_eco(n):
    last_one = 1
    last_two = 0
    for x in range(1, n):
        tmp = last_two
        last_two = last_one
        last_one += tmp

    return last_one


start = time.time()
print(fib_hard(28))
end = time.time()
print((end - start))

start2 = time.time()
print(fib_eco(28))
end2 = time.time()
print((end2 - start2))
