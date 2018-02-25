import requests

requests.get("http://braincad.com/")

r = requests.get("http://braincad.com/")

print(r.content[:50])