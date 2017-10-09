# Functions


def func_name(parameters=False):
    """docstring"""
    if parameter:
        return parameters
    else:
        return None


func_name()
print(func_name.__doc__)
print(func_name.__name__)


def tags(x):
    return [a.strip(" !@#$%^&*()_+-=.") for a in x.split(",")]


print(tags("python, coursera, mooc"))

# annotations
# def func_name(parameter1:type, parameter2:type = "default_value") -> type
# but, other types still works -> just for IDE/debugging

# parameters is referenced. Use return, Luke!
# parameters could be named

# Scoping
#   each scope has its own namespace
#   local

# Default values
#   Avoid using mutable types (lists, sets, dicts) as default values

# print(func_name().__default__)


def printer(*args):
    print(type(args))
    for i in args:
        print(i)


name_list = ["Вася", "Петя", "Миша"]
printer(*name_list)


def printer2(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, ":", value)

printer2(a=10,b=11)

