import os
import tempfile
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--key", help="Sets a key to store or get")
parser.add_argument("--value", help="Optional. If present, stored at the key")
args = parser.parse_args() # args.(key|value)

storage_filename = os.path.join(tempfile.gettempdir(), 'storage.data')
if not(os._exists(storage_filename)):
    with open(storage_filename, 'a') as f:
        pass

def get(key):
    result = []
    k = ""
    v = ""
    lines = []
    with open(storage_filename, 'r') as f:
        lines = f.readlines()
    for line in lines:
        (k, v) = line.split(",")
        if k == key: result.append(v.strip("\n ,"))
    if result:
        print(", ".join(result))
    else:
        print(None)


def store(key, value):
    with open(storage_filename, 'a') as f:
        f.write(",".join([key, value])+"\n")


if args.value and args.key:
    store(args.key, args.value)
elif args.key:
    get(args.key)
