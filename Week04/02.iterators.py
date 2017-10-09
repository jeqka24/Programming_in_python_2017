# 01. iterators  - object with

a = iter([1,2,3])

class SquareIterator:
    def __init__(self, start, stop):
        self.current = start
        self.end = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return  result

for x in SquareIterator(1,4):
    print(x,end=",")

print()

class IndexIterator:
    def __init__(self,obj):
        self.obj = obj

    def __getitem__(self,index):
        return self.obj[index]

for x in IndexIterator("String"):
    print(x,end="")