#!/bin/bash
mkdir -p /tmp/hyprlang/
cd /home/minoru/.config/hypr/
python hyprconf.py &
python hypridle.py &
python hyprlock.py &
python hyprpaper.py &

mkdir -p /tmp/hypr/
cd ~
export _JAVA_AWT_WM_NONREPARENTING=1
Hyprland --config /tmp/hyprlang/hyprland.conf
