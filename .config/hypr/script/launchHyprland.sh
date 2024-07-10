#!/bin/bash
mkdir -p /tmp/hyprlang/
cd /home/minoru/.config/hypr/
exec_once(){
    local cmd=$1
    pgrep -f $cmd > /dev/null || ($cmd &)
}
exec_once "python hyprconf.py"

mkdir -p /tmp/hypr/
cd ~
export _JAVA_AWT_WM_NONREPARENTING=1
Hyprland --config /tmp/hyprlang/hyprland.conf
