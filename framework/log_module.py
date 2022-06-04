from time import time

from patterns.singleton import SingletonNamed


class Logger(metaclass=SingletonNamed):

    def __init__(self, name):
        self.name = name

    def log(self, text):
        print('log--->', text)


def debug(func):
    def wrap(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print('DEBUG -> ', func.__name__, end - start)
        return result
    return wrap

# s1, s2, s3 = Logger('log_1'), Logger('log_2'), Logger('log_1')
# print(s1, '\n', s2, '\n', s3, sep='')
# print(s1 is s3)
