#!/bin/bash

if [[ $# -eq 0 || $# -gt 2 ]]; then
    echo "Error: 1 or 2 arguments required"
    exit 1
fi
wallpaper=$1
monitor=""
if [ $# -eq 2 ]; then
    monitor=$1
    wallpaper=$2
fi
wallpaper=$(realpath "$wallpaper")
hyprctl hyprpaper unload all 
hyprctl hyprpaper preload "$wallpaper"
hyprctl hyprpaper wallpaper "$monitor,$wallpaper" && wallust -s run "$wallpaper" || echo "Error: Failed to set wallpaper"
 

