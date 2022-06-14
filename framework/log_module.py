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


class ConsoleWriter:

    def write(self, text):
        print(text)


class FileWriter:

    def __init__(self, file_name):
        self.file_name = file_name

    def write(self, text):
        with open(self.file_name, 'a', encoding='utf-8') as f:
            f.write(f'{text}\n')
