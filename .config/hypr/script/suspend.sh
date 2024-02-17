#!/bin/bash

swayidle -w \
    timeout 1 'hyprctl dispatch dpms on' \
    timeout 120 'hyprctl dispatch dpms off' \
    timeout 300 'swaylock \
    --screenshots \
    --effect-blur 7x5 \
    --effect-vignette 0.5:0.5 \
    --ring-color bb00cc \
    --key-hl-color 880033 \
    --line-color 00000000 \
    --inside-color 00000088 \
    --separator-color 00000000 \
    --grace 2 \
    --fade-in 0.2 &' \
    timeout 600 'systemctl suspend' \
    resume 'hyprctl dispatch dpms on' \
    before-sleep 'hyprctl dispatch dpms off' \

# swayidle -w \
#     timeout 1 'hyprctl dispatch dpms on' \
#     timeout 120 'hyprctl dispatch dpms off' \
#     resume 'hyprctl dispatch dpms on' \
#     before-sleep 'hyprctl dispatch dpms off' \

