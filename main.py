import requests
import json
from printer import *
import pyfiglet


def user_info(user_id,flag):
  if flag:
    url = "https://api.github.com/users/{}/repos".format(user_id)
    r = requests.get(url)
    repos = json.loads(r.text)
    for repo in repos:
      print(repo["name"])
      print("\tDescription: "+str(repo["description"]))
      print("\tOwner: "+str(repo["owner"]["login"]))
      print("\tForks Count: "+str(repo["forks_count"]))
      print("\tWatch Count: "+str(repo["watchers_count"]))


<<<<<<< HEAD
def email_to_user(email_id):
  userid = "https://api.github.com/search/users?q={}".format(email_id)
  r = requests.get(userid)
  users=json.loads(r.text)
  if users["total_count"]!=1:
    print("invalid email-id provided")
    return 0
  
  user_id = users["items"][0][""] 






  user_url = "https://api.github.com/users/rishabhryber"
=======

  user_url = "https://api.github.com/users/{}".format(user_id)
>>>>>>> 987fadaeaef4f252746b044b8d90d9ff072f2a84
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

def email_to_id(email):
  url = "https://api.github.com/search/users?q={}".format(email)
  r = requests.get(url)
  users = json.loads(r.text)
  if users["total_count"] != 1:
    print("Invalid email id provided")
    return
  user = users["items"][0]
  email = user["login"]
  return email
  
def show_man():
  print_color("-------------------------------------************--------------------------------\n","green")
  banner = pyfiglet.figlet_format("git - it")
  print_color(banner,"green")
  print_color("-------------------------------------************--------------------------------\n","green")
  print_color("Help:::","green")
  print_color("\tUsages: python git-it [options] [parameter]")
  print_color("\t Options")
  print_color("\t\t-u, -U\n\t\t\t Use the github user-id is provided")
  print_color("\t\t-e, -E\n\t\t\t Use the email id")
  print_color("\t\t-r, -R\n\t\t\t Show repository details also")

def show_logo():
  print_color("-------------------------------------************--------------------------------\n","red")
  banner = pyfiglet.figlet_format("git - it")
  print_color("    "+banner,"green")

def repo_url_to_info(strurl,flag):
  str1=strurl.split("/")
  username=str1[3]
  repo=str1[4]
  if flag==0:
    user_info(username,0)
  elif flag==1:
    user_info(username,1)





