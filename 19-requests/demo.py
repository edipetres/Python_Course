import requests

url = ''

r = requests.get(url)

print(r.url)
print(r.status_code)
print(r.json)