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
#        lines.remove("ok")
        for line in lines[1:]:
            if line:
                (key, val, ts) = line.split(" ")
                a = result.get(key)
                if a:
                    result[key].append((int(ts), float(val)))
                else:
                    result[key] = [(int(ts), float(val)), ]
        return result

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def put(self, key, value, timestamp=time.time()):
        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            try:
                prepared = "put {} {} {}\n".format(key, value, str(int(timestamp))).encode("utf-8")
                sock.send(prepared)
                response = sock.recv(1024).decode("utf-8")
                if error(response):
                    raise ClientError("Wrong command")
            except OSError as e:
                print("Error:", e.strerror, e.args)

    def get(self, metric):
        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            try:
                prepared = f"get {metric}\n".encode("utf-8")
                sock.send(prepared)
                g = sock.recv(1024).decode("utf-8")
                if g[0:2] == "ok":
                    responce = Client.parse(g)
                else:
                    raise ClientError
            except OSError as e:
                print("Error:", e.strerror, e.args)
                responce = {}
        return responce

class ClientError(Exception):
    pass


if __name__ == "__main__":
    client = Client("127.0.0.1", 8181, timeout=15)

    client.put("palm.cpu", 0.5, timestamp=1150864247)
    client.put("palm.cpu", 2.0, timestamp=1150864248)
    client.put("palm.cpu", 0.5, timestamp=1150864248)

    client.put("eardrum.cpu", 3, timestamp=1150864250)
    client.put("eardrum.cpu", 4, timestamp=1150864251)
    client.put("eardrum.memory", 4200000)

    print(client.get("palm.cpu"))
    print(client.get("eardrum.cpu"))
    print(client.get("*"))
