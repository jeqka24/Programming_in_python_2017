# with ___ as f:
#   something()

class open_file:
    def __init__(self, filename, mode="r"):
        self.f = open(filename,mode)

    def __enter__(self):
        return self.f

    def __exit__(self, *args):
        self.f.close()

with open_file("test.log","w") as f:
    f.write("Inside context manager 'open_file'")

# ? can i wrap magic (__something__) methods in decorators? for example, logging or another dependency injection
#

# see contextlib - library of context managers

import time


class timer():
    def __init__(self):
        self.start = time.time()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        print("Elapsed time:", self.current_time())
        pass

    def current_time(self):
        return time.time() - self.start


with timer() as t:
    time.sleep(1.0)
    print(t.current_time())
    time.sleep(1.0)
