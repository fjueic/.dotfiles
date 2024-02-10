#!/bin/sh

# This script is used to notify the user when the battery is low, full, charging or discharing.

export DISPLAY=:0
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus 


# Get the battery status
status=$(upower -i /org/freedesktop/UPower/devices/battery_BAT0 | grep -E "state" | awk '{print $2}')

if [ $status = "charging" ]; then
  exit 0
fi

level=$(upower -i /org/freedesktop/UPower/devices/battery_BAT0 | grep -E "percentage" | awk '{print $2}' | sed 's/%//g')

if [ $status = "discharging" ]; then
  if [ $level -le 10 ]; then
    notify-send -u critical "Battery is low" "Battery level is ${level}%"
  fi
fi

