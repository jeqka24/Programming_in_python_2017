from threading import Thread

import time

def count(n):
    while n>0:
        n -= 1


# series run
t0 = time.time()
count(100_000_000)
count(100_000_000)
print(time.time() - t0)

# parallel run
t0 = time.time()
th1 = Thread(target=count, args=(100_000_000,))
th2 = Thread(target=count, args=(100_000_000,))
th1.start(); th2.start()
th1.join(); th2.join()
print(time.time() - t0)

# cpu-bound threads takes more time to complete
# io-bound threads takes less time

# thread calls takes GIL
# system calls do not aquire GIL

# SEE ALSO:
# * multiprocessing
# * threading
# * concurrent.futures