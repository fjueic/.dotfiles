#!/bin/bash

# Check if the folder path is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <folder-path>"
    exit 1
fi

sleep 3
# Get the folder path
FOLDER_PATH="$1"

# Check if the folder exists
if [ ! -d "$FOLDER_PATH" ]; then
    echo "Error: Folder '$FOLDER_PATH' does not exist."
    exit 1
fi

# Infinite loop to shuffle and change wallpapers
while true; do
    # Shuffle the list of wallpapers
    SHUFFLED_WALLPAPERS=$(find "$FOLDER_PATH" -type f | shuf)

    # Loop through each shuffled wallpaper
    for WALLPAPER in $SHUFFLED_WALLPAPERS; do
        ~/.config/hypr/script/change_wallpaper.sh "$WALLPAPER"
        echo "Wallpaper changed to: $WALLPAPER"
        sleep 300
    done
done

