#!/bin/bash

git --git-dir=/home/minoru/Obsidian/.git --work-tree=/home/minoru/Obsidian add .
git --git-dir=/home/minoru/Obsidian/.git --work-tree=/home/minoru/Obsidian commit -m "auto commit"
git --git-dir=/home/minoru/Obsidian/.git --work-tree=/home/minoru/Obsidian push origin main

# notify-send "Sync" "Synced notes to GitLab"
