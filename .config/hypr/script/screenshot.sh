#!/bin/bash

# image path ~/Pictures/Screenshots/$(date +%s).png

image_path=~/Pictures/Screenshots/$(date +%s).png

grim -g "$(slurp)" "$image_path"

wl-copy < "$image_path"
