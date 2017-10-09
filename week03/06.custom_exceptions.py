import sys
import requests

#

url = sys.argv[1]

responce = requests.get(url)

print(responce.content, timeout=30)