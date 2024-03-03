#!/usr/bin/env python3
import pyudev
import os

TURN_OFF_HYPRLAND_ANIMATIONS = "~/.config/hypr/script/turn_off_hyprland_animations.sh"
TURN_ON_HYPRLAND_ANIMATIONS = "~/.config/hypr/script/turn_on_hyprland_animations.sh"

NOTIFY_ONLINE = "notify-send -i battery-charging-symbolic 'Power Supply Online' 'Hyprland animations are now enabled'"
NOTIFY_OFFLINE = "notify-send -i battery-empty-symbolic 'Power Supply Offline' 'Hyprland animations are now disabled'"

def monitor_udev_events():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='power_supply')
    for device in iter(monitor.poll, None):
        if 'POWER_SUPPLY_ONLINE' in device:
            power_supply_online = device.get('POWER_SUPPLY_ONLINE')
            if power_supply_online == '1':
                os.system(TURN_ON_HYPRLAND_ANIMATIONS)
                os.system(NOTIFY_ONLINE)
            else:
                os.system(TURN_OFF_HYPRLAND_ANIMATIONS)
                os.system(NOTIFY_OFFLINE)
if __name__ == "__main__":
    monitor_udev_events()

