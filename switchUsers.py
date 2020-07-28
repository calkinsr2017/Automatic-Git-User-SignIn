import subprocess
import os


ssh = input("Enter your SSH key name: ")
userName = input("Enter your github username: ")
email = input("Enter your github email: ")
#repo = input("Paste in the github repo that you are working on (with owner name!): ")
repo = ""
with open("remote_origin_url.txt", "w") as file:
    #create the file
    subprocess.run(["git", "config", "--get", "remote.origin.url"], stdout = file)

url_file = open("remote_origin_url.txt", "r")
if url_file.mode == 'r':
    url = url_file.read()
    
    if "https://" in url:
        githubSubstring = "https://github.com/"
        repo = url[len(githubSubstring)::]
        
    else:
        repo = url[url.find(':') + 1::]

repo = repo.rstrip("\n")

fullString = "git@github-" + ssh + ":" + repo

subprocess.run(["git", "remote", "set-url", "origin", fullString])
subprocess.run(["git", "config", "--replace-all", "user.name",  userName])
subprocess.run(["git", "config", "--global", "--replace-all", "user.name", userName])
subprocess.run(["git", "config", "--replace-all", "user.email", email])
subprocess.run(["git", "config", "--global", "--replace-all", "user.email", email])
subprocess.run(["git", "remote", "-v"])