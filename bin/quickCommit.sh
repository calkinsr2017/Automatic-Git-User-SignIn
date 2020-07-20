#!/bin/bash

git pull
git add .  
git add -u
read -e -p "Commit description: " desc
git commit -m "$desc"
git push

