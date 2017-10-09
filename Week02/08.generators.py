def gen1(start, end):
    current = start
    while current < end
        yield current
        current += 2


for number in gen1(0, 10):
    print(number)


def fibo(n):
    a = b = 1
    for _ in range(number):
        yield b
        a, b = b, a + b

def accum():
    total = 0
    while True:
        value = yield total
        print ("Got: {}".format(value))
        if not value: break
        total += value

generator = accum()
next(generator) # required to start accumulating
print("accumulated: {}".format(generator.send(12)))