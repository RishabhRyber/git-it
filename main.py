import requests
import json
url = "https://api.github.com/users/rishabhryber/repos"
r = requests.get(url)
repos = json.loads(r.text)
for repo in repos:
  print(repo["name"])
  print("\tDescription: "+repo["description"])
  print("\tOwner: "+repo["owner"]["login"])
  print("\tClone URL: "+repo["clone_url"])

  print("\tForks Count: "+str(repo["forks_count"]))
  print("\tWatch Count: "+repo["watchers_count"])
  print("\tClone URL: "+repo["clone_url"])
 # print("\tClone URL: "+repo["clone_url"])
