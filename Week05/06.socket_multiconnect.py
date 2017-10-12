# fails under windows
import socket
import threading
import multiprocessing
import os


def process_request(conn,addr):
    print("connected client:", addr)
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode("utf8"))


def worker(sock):
    conn, addr = sock.accept()
    print("pid:", os.getpid())
    th = threading.Thread(target=process_request, args=(conn, addr))
    th.start()


with socket.socket() as sock:
    sock.bind(("", 10001))
    sock.listen()

    worker_count = 4
    worker_list = [multiprocessing.Process(target=worker, args=(sock,)) for _ in range (worker_count)]

    for w in worker_list:
        w.start()

    for w in worker_list:
        w.join()