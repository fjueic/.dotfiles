#!/bin/sh

if [ -z "$XDG_RUNTIME_DIR" ]; then
  export XDG_RUNTIME_DIR=/run/user/$(id -u)
fi







enable_device ()
{
  HYPRLAND_VARIABLE="device:$1:enabled"
  notify-send -u normal "Enabling $1"
  hyprctl keyword $HYPRLAND_VARIABLE true
}

disable_device ()
{
  HYPRLAND_VARIABLE="device:$1:enabled"
  notify-send -u normal "Disabling $1"
  hyprctl keyword $HYPRLAND_VARIABLE false
}

get_device_status ()
{
  hyprctl getoption $1 | grep 'int: 1'
}

get_all_mice ()
{
  hyprctl devices | python3 ~/.config/hypr/script/get_all_mice.py
}

turn_off_all_mice ()
{
  for mouse in $(get_all_mice); do
    disable_device $mouse
  done
}

turn_on_all_mice ()
{
  for mouse in $(get_all_mice); do
    enable_device $mouse
  done
}

# check for command line arguments
if [ $# -eq 0 ]; then
  echo "Usage: $0 [on|off]"
  exit 1
fi


case "$1" in
  on)
    turn_on_all_mice
    ;;
  off)
    turn_off_all_mice
    ;;
  *)
    echo "Usage: $0 [on|off]"
    exit 1
    ;;
esac
