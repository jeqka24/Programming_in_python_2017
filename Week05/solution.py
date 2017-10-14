# asyncio tools:
#  - event loop (get_event_loop() )
#  - Future
#  - Task
#  - open_connection(host,port,event_loop)
#  - @asyncio.coroutine
# working with

import socket
import time


def ok(x):
    return x == "ok\n\n"


def error(x):
    return x == "error\nwrong command\n\n"


class Client:
    @staticmethod
    def parse(request): # String -> dict
        result = {}
        lines = request.split("\n")
        lines.remove("ok")
        lines.remove("")
        lines.remove("")
        for line in lines:
            (key, val, ts) = line.split(" ")
            a = result.get(key)
            if a:
                result[key].append((ts, val))
            else:
                result[key] = [(ts, val), ]
        return result

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def put(self, key, value, timestamp=time.time()):
        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            try:
                prepared = "put {} {} {}".format(key, value, str(int(timestamp))).encode("utf-8")
                print("put:", prepared)
                sock.send(prepared)
                responce = sock.recv(1024).decode("utf-8")
                if error(responce):
                    raise ClientError("Wrong command")
            except OSError as e:
                print("Error:", e.strerror, e.args)

    def get(self, metric):
        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            try:
                prepared = f"get {metric}".encode("utf-8")
                sock.send(prepared)
                g = sock.recv(1024).decode("utf-8")
                responce = Client.parse(g)
            except OSError as e:
                print("Error:", e.strerror, e.args)
                responce = {}
        return responce

class ClientError(Exception):
    pass


metrics_for_put = [
    ("test", 0.5, 1),
    ("test", 2.0, 2),
    ("test", 0.4, 2),
    ("load", 301, 3),
]

if __name__=="__main__":
    print(Client.parse("ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n"))
    cl = Client("localhost", 8000, 4)
    for (key, value, ts) in metrics_for_put:
        cl.put(key, value, ts)
    for key in ["*", "test", "load"]:
        print("Key:", key," value:", cl.get(key))

    cl.put("palm.cpu", 0.5, timestamp=1150864247)
    cl.put("palm.cpu", 2.0, timestamp=1150864248)
    cl.put("palm.cpu", 0.5, timestamp=1150864248)

    cl.put("eardrum.cpu", 3, timestamp=1150864250)
    cl.put("eardrum.cpu", 4, timestamp=1150864251)
    cl.put("eardrum.memory", 4200000)

    cl.get("*")