#!/bin/bash

image_path=~/Pictures/Screenshots/$(date +%s).png

arg="$1"

if [ "$arg" = 1 ]; then
    grim -g "$(slurp)" "$image_path"
else
    grim -g "0,0 1920x1080" "$image_path"
fi

echo "$image_path" | wl-copy # Copy image path to clipboard
wl-copy < "$image_path"
