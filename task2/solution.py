from collections import OrderedDict
from itertools import count


def groupby(function, xs):
    keys = list(map(function, xs))
    dictonary = {}
    for key in keys:
        values_of_the_key = [x for x in xs if function(x) == key]
        dictonary[key] = values_of_the_key
    return dictonary


def iterate(func):
    current = lambda x: x
    while True:
        yield current
        current = comp(func, current)


def comp(first, second):
    return lambda x: first(second(x))


def zip_with(func, *iterables):
    return (func(*args) for args in zip(*iterables))


def cache(func, cache_size):
    cached_arguments = OrderedDict()

    def func_cached(*args):
        if args not in cached_arguments:
            if len(cached_arguments) == cache_size:
                cached_arguments.popitem(last=False)
            cached_arguments[args] = func(*args)
        return cached_arguments[args]
    return func_cached
