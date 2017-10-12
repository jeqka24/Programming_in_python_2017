# epoll. linux only

# moving on asyncio

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