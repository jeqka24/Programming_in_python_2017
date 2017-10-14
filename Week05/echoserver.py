import socket
import threading

db={}

def process_get(request):
    key = request[0]
    responce = b"ok\n"
    if key=="*":
        for key in db:
            for (ts, value) in db[key]:
                responce += "{} {} {}\n".format(key, value, ts).encode("utf-8")
    elif db.get(key):
        for (ts, value) in db[key]:
            responce += "{} {} {}\n".format(key, value, ts).encode("utf-8")
    else:
        pass
    responce += b"\n"
    return responce


def process_put(request):
    (key,value, ts) = tuple(request)
    a = db.get(key)
    if a:
        db[key].append((ts, value))
    else:
        db[key] = [(ts, value), ]
    return b"ok\n\n"

def process_request(conn, addr):
    print("connected client:", addr)
    with conn:
        while True:
            rawdata = conn.recv(1024)
            if not rawdata:
                break
            data = rawdata.decode("utf-8").split(" ")
            command = data[0]; del(data[0])
            if command == "get":
                conn.send(process_get(data))
            elif command == "put":
                conn.send(process_put(data))
            else:
                conn.send(b"error\nwrong command\n\n")
            print(rawdata.decode("utf-8"))

with socket.socket() as sock:
    sock.bind(("", 8000))
    sock.listen()
    while True:
        conn, addr = sock.accept()
        th = threading.Thread(target=process_request, args=(conn, addr))
        th.start()