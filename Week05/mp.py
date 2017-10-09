from multiprocessing import Process


def f(name):
    print("Hello, {}".format(name))

if __name__ == '__main__':
    p = Process(target=f, args=("Bob",))
    p.start()
    p.join()
