import subprocess
import os




desc = input("Commit description: ")


subprocess.run(["git", "pull"])
subprocess.run(["git", "add", "."])
subprocess.run(["git", "add", "-u"])
subprocess.run(["git", "commit", "-m", desc])
subprocess.run(["git", "push"])

