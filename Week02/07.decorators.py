# minimal:
# takes function as parameter and returns function


#def decorator(func):
#    return func

#@decorator
#def decorated():
#    print("Hello!")

# decorated = decorator(decorated)


def decorator2(func):
    def new_func():
        pass
    return new_func()


def logger(func):
    def wrapped(num_list):
        result = func(num_list)
        with open('log.txt', 'wa') as f:
            f.write(str(result))
        return result
    return wrapped


@logger
def summator(num_list):
    return sum(num_list)


import functools


def unilogger(func):
    @functools.wraps(func)
    def wrapped(*args,**kwargs):
        result = func(*args, **kwargs)
        with open('log.txt', 'wa') as f:
            f.write(str(result))
        return result
    return wrapped


@unilogger
def summator(num_list):
    return sum(num_list)


def file_logger(filename):
    def decorator(func):
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'w+') as f:
                f.write(str(result))
            return result
        return wrapped
    return decorator

print("summator: {}".format(summator([1,2,3,4,])))
print(summator.__name__)

@file_logger("summator.log")
def summ2file(num_list):
    return sum(num_list)

def dec1(func):
    def wrapped():
        print("1:",)
        return func()
    return wrapped

def dec2(func):
    def wrapped():
        print("2:",)
        return func()
    return wrapped
