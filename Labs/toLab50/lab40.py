import functools
from datetime import datetime


def create_fun_wrapper(fun):
    def fun_wrapper(*args, **kwargs):
        start = datetime.now()
        result = fun(*args, **kwargs)
        end = datetime.now()
        print('Time worked function {} is:'.format(fun.__name__), end - start)
        return result

    return fun_wrapper


@create_fun_wrapper
def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v


get_sequence(15)
