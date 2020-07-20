import requests

url = "https://api.openstreetmap.org/api/0.6/node/1441267732"

response = requests.get(url)
print(response.status_code)
print(type(response.status_code))
print(response.text)