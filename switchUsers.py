import subprocess


ssh = input("Enter your SSH key name: ")
userName = input("Enter your github username: ")
email = input("Enter your github email: ")
repo = input("Paste in the github repo that you are working on: ")

fullString = "git@github-" + ssh + ":" + repo

subprocess.run(["git", "remote", "set-url", "origin", fullString])
subprocess.run(["git", "config", "user.name", userName])
subprocess.run(["git", "config", "user.email", email])


