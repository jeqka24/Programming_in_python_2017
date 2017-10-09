# Thread syncing
# 1. Using

from queue import Queue
from threading import Thread

def worker(queue,n):
    while True:
        item = queue.get()
        if item is None:
            break
        print("Process data:", n, item)

q = Queue(5)

th1 = Thread(target=worker, args=(q, 1))
th2 = Thread(target=worker, args=(q, 2))
th1.start()
th2.start()

for i in range(50):
    q.put(i)

q.put(None);q.put(None)

th1.join(); th2.join()

# 2. Semaphoring - RLock

import threading

class Point(object):
    def __init__(self):
        self._mutex = threading.RLock()
        self._x = 0
        self._y = 0

    def get(self):
        with self._mutex:
            return self._x, self._y

    def set(self, x, y):
        with self._mutex:
            self._x = x
            self._y = y

# 3. multithread queues

class Q(object):
    def __init__(self, size = 5):
       self._size = size
       self._queue = []
       self._mutex = threading.RLock()
       self._empty = threading.Condition(self._mutex)
       self._full = threading.Condition(self._mutex)

    def put(self, val):
        with self._full:
            while len(self._queue) >= self._size:
                self._full.wait()
            self._queue.append(val)
            self._empty.notify()

    def get(self):
        with self._empty:
            while len(self._queue) == 0:
                self._empty.wait()
            ret = self._queue.pop()
            self._full.notify()
            return ret