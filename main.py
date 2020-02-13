import requests
import json

def user_info(user_id,flag):
  if flag:
    url = "https://api.github.com/users/{}/repos".format(user_id)
    r = requests.get(url)
    repos = json.loads(r.text)
    for repo in repos:
      print(repo["name"])
      print("\tDescription: "+str(repo["description"]))
      print("\tOwner: "+str(repo["owner"]["login"]))
      print("\tClone URL: "+repo["clone_url"])

      print("\tForks Count: "+str(repo["forks_count"]))
      print("\tWatch Count: "+str(repo["watchers_count"]))
      print("\tClone URL: "+str(repo["clone_url"]))
    # print("\tClone URL: "+repo["clone_url"])


  user_url = "https://api.github.com/users/rishabhryber"
  r = requests.get(user_url)
  user = json.loads(r.text)
  print("Name: "+str(user["name"]))
  print("Bio: "+str(user["bio"]))
  print("Blog: "+str(user["blog"]))
  print("Followers Count: "+str(user["followers"]))
  print("Location: "+str(user["location"]))
  print("Public Repos Count: "+str(user["public_repos"]))
  print("Joined on : "+str(user["created_at"]))
  print("Last Active : "+str(user["updated_at"]))
