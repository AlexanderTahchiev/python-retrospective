def groupby(function, xs):
    keys = list(set(map(function, xs)))
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
