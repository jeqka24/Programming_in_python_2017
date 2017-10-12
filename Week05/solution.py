# asyncio tools:
#  - event loop (get_event_loop() )
#  - Future
#  - Task
#  - open_connection(host,port,event_loop)
#  - @asyncio.coroutine
# working with

import socket
import time
import re

#
ok = lambda x: x == "ok\n\n"
error = lambda x: x == "error\nwrong command\n\n"


#regex_values = re.findall(r'^ok\n(.*?\n)+$',html)


class Client:
    def __init__(self, host, port, timeout=15):
        self.conn, self.addr = socket.create_connection((host,port),timeout=timeout)
        pass

    def put(self, key, value, timestamp=time.time()):
        try:
            self.conn.send("put {} {} {}".format(key, value, str(int(timestamp))).encode())
            responce = self.conn.recv().decode()
            print(responce)
        except OSError as e:
            print("Error:", e.strerror, e.args)
        return

    def get(self, metric):
        try:
            self.conn.send(f"get metric".encode())
            responce = self.conn.recv().decode()
        except OSError as e:
            print("Error:", e.strerror,e.args)
        pass

class ClientError(Exception):
    pass
