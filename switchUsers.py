import subprocess

ssh = input("Enter your SSH key name: ")
userName = input("Enter your github username: ")
email = input("Enter your github email: ")
repo = input("Paste in the github repo that you are working on (with owner name!): ")

fullString = "git@github-" + ssh + ":" + repo + ".git"

subprocess.run(["git", "remote", "set-url", "origin", fullString])
subprocess.run(["git", "config", "user.name", "--replace-all", userName])
subprocess.run(["git", "config", "--global", "--replace-all", "user.name", userName])
subprocess.run(["git", "config", "--replace-all", "user.email", email])
subprocess.run(["git", "config", "--global", "--replace-all", "user.email", email])
