import functools
from datetime import datetime

global_path = r'C:\Python\experiments\exp\logs-lab41'


def create_wrapper_to_wrapper(pth):
    def create_wrapper(fun):
        def the_fun(*args, **kwargs):
            time = datetime.now()
            result = fun(*args, **kwargs)
            print('Action function {} executed on {} on time: {}'.format(fun.__name__, pth, time))
            return result
        return the_fun
    return create_wrapper
# def create_wrapper(fun):
#         def the_fun(*args, **kwargs):
#             time = datetime.now()
#             result = fun(*args, **kwargs)
#             print('Action function {} executed on {} on time: {}'.format(fun.__name__, pth, time))
#             return result


@create_wrapper_to_wrapper(global_path)
def file_creator(path, name='name'):
    # name = '\\' + name if name is not None else False
    name = name + '.txt'
    file = open(path + '\\' + name, 'a')
    file.close()
    return name


@create_wrapper_to_wrapper(global_path)
def file_delete(path, name='name'):
    import os
    name = name + '.txt'
    os.remove(path + '\\' + name)
    return os.listdir(path)


x = 'xyz'
print(file_creator(global_path, x))
print(file_creator(global_path, x + x))
print(file_creator(global_path, x + 'a'))
print(file_delete(global_path, x))
print(file_creator(global_path, x))

