import asyncio
import threading

class AsyncDb(dict):
    def __init__(self):
        self._mutex = threading.RLock()
        self._db = {}

    def get(self):
        with self._mutex:
            return self._db

    def set(self, db):
        with self._mutex:
            self._db = db


adb = AsyncDb()
db = {}

def process_get(request):
    print("get request:", request[0])
    key = request[0]
    response = "ok\n"
    if key == "*":
        for key in db:
            for (ts, value) in db[key]:
                response += "{} {} {}\n".format(key, value, ts)
    elif db.get(key, False):
        for (ts, value) in db[key]:
            response += "{} {} {}\n".format(key, value, ts)
    else:
        pass
    response += "\n"
    print("Get result:", response)
    return response


def process_put(request):
    (key, value, ts) = tuple(request)
    a = db.get(key)
    if a:
        db[key].append((ts, value))
    else:
        db[key] = [(ts, value), ]
    return "ok\n\n"


def process_data(request): # # string -> string
    data = request.split(" ")
    command = data[0]; del(data[0])
    if command == "get":
        result = process_get(data)
    elif command == "put":
        result = process_put(data)
    else:
        result = "error\nwrong command\n\n"
    return result


class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        req = data.decode()
        print("Request:",req)
        resp = process_data(req)
        print("Responce:", resp.encode())
        self.transport.write(resp.encode())


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

if  __name__ == "__main__":
    run_server("127.0.0.1", 8181)
