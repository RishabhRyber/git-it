import requests
import json

url = "https://api.github.com/users/rishabhryber/repos"
r = requests.get(url)
print(r.text)