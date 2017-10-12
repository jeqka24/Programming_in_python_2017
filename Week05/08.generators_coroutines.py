
# Remembering an iterator-way
class MyRangeIterator:
    def __init__(self, top):
        self.top = top
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= top:
            raise StopIteration

        current = self.current
        self.current += 1
        return current

# remembering a generator-way
def MyRangeGenerator(top):
    current = 0
    while current < top:
        yield current
        current += 1


# coroutine
def grep(pattern):
    print("start grep")
    try:
        while True:
            line = yield
            if pattern in line:
                print(line)
    except GeneratorExit:
        print("stop grep")

def grep_python_coroutine():
    g = grep("python")
    yield from g

g = grep_python_coroutine("python")

next(g) # g.send(None)

g.send("golang is bettar!")
g.send("python is simple!")
g.throw(RuntimeError, "something went wrong!")


# Несмотря на некоторую схожесть, у генератора и корутины два важных отличия:
#    Генераторы "производят" значения (yield item)
#    Корутины "потребляют" значения (item = yield)

# Корутина может иметь два состояния: suspended и resumed
# yield приостанавливает корутину
# send() возобновляет работу корутины
# close() завершает выполнение
# yield from используется для делегирования вызова генератора
