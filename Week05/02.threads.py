# import threading
# ThreadPoolProcess

#  all threads share memory and resources of main

from threading import  Thread

def f(name):
    print("Hello, {}".format(name))

th = Thread(target=f,args=("Bob",))
th.start()
th.join()

class PrintThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print("Hello, {}".format(self.name))


if __name__ == '__main__':
    p = PrintThread("Mike")
    p.start()
    p.join()



# Thread Pool

from concurrent.futures import ThreadPoolExecutor, as_completed

def ff(a):
    return a*a

# .shutdown() on exit

with ThreadPoolExecutor(max_workers=3) as pool:
    results = [pool.submit(ff,i) for i in range(10)]

    for future in as_completed(results):
        print(future.result())