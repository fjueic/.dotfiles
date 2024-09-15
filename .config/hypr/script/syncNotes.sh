#!/bin/bash

git --git-dir=/home/minoru/notes/.git --work-tree=/home/minoru/notes add .
git --git-dir=/home/minoru/notes/.git --work-tree=/home/minoru/notes commit -m "auto commit"
git --git-dir=/home/minoru/notes/.git --work-tree=/home/minoru/notes push origin main

# notify-send "Sync" "Synced notes to GitLab"
