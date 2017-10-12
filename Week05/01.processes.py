# processes has parameters
#  - PID
#  - memory
#  - strace
#  - lsof -p PID -
#  - top, ps uax

# Tools:
# 1. os.fork()
# 2. multiprocessing.Process

import os
import time

foo = "bar"

pid = os.fork()
print(pid)
if pid == 0:
    # daughter process

    while True:
        foo = "baz"
        print("child:", foo)
        time.sleep(5)
else:
    print("parent:", foo)
    os.wait() # wait for

# fork copies memory and file descrip
# expected output:
#   parent:bar
#   child:baz
# the same is for file descriptors

from multiprocessing import Process

def f(name):
    print("Hello, {}".format(name))

p = Process(target=f, args=("Bob",))
p.start()
p.join()

# see mp.py and mp2.py