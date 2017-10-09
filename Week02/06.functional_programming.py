# 1. functions as first-class objects

def caller(func, params):
    return func(*params)


def printer(name,origin):
    print("{} - {}".format(name, origin))


def get_multiplier():
    def inner(a, b):
        return a*b
    return inner

multiplier = get_multiplier()
multiplier(10,11)

# multiplier.__name__ == "inner"

# Замыкание - continuations
def get_multiplier2(number):
    def inner(a):
        return a*number
    return inner

# 2. map, filter, lambda

def squarify(a):
    return a ** 2

# map(func, iterable) -> iterable (map_object)
# list(map(squarify, range(5)))
# [0, 1, 4, 9, 16]

# filter ( func_bool, iterable) -> iterable
# list(filter(lambda a:a>0, range(-10,10))

# zip(iterable,iterable0 -> tuple
# Use it with caution, Luke!

def stringifier(num_list):
    return list(map(str,num_list))

# 3. functools
# reduce
from functools import reduce
reduce(lambda x,y:x*y, range(1,10))

# partial - create sub-functions, corner-cases
from functools import partial
def greeter(name, greeting):
    return "{}, {}!".format(greeting, name)

hier = partial(greeter, greeting='Hi')
helloer = partial(greeter, greeting='Hello')

print(hier("brother"))
print(helloer("sir"))

# Proceed with caution!
# Списочные выражения
a = [number ** 2 for number in range(10)]
# ... и с условием
a = [number ** 2 for number in range(10) if number % 2 == 0]



