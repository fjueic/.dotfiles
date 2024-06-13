from Hyprlang import *

config = Hyprlang_config(__file__)
def blue_light_filter():
    from os import system
    system("hyprshade on blue-light-filter")
config.add_side_effect(blue_light_filter)
config.add_via_primitive(
    **{"exec-once": [
        # lock on boot
        ["hyprlock || hyprctl dispatch exit"],
        # create virtual monitor
        ["hyprctl output create headless"],
        # wayvnc
        ["pidof wayvnc || wayvnc -g 0.0.0.0"],
        # hypridle
        ["(killall hypridle || true) && hypridle"],
        ["(pidof waybar || waybar)"],
        ["(pidof hyprpaper|| hyprpaper)"],
        ["/usr/lib/polkit-kde-authentication-agent-1"],
        ["gnome-keyring-daemon --start --components=secrets"],
        ["blueman-applet"],
        ["nm-applet --indicator"],
        ["/usr/lib/kdeconnectd"],
        ["/usr/bin/kdeconnect-indicator"],
        ["~/.config/hypr/script/change_all_mice_state.sh on"],
        ["~/.config/hypr/script/spin_up_markdown_preview_server.sh"],
        # commands to run when the power plug is plugged in or out
        ["~/.config/hypr/script/power_plug_in_and_out.py"],
        # battery monitor
        ["~/.config/hypr/script/monitor_battery.py"],
        # clipboard manager
        ["wl-paste --type text --watch cliphist store"],
        ["wl-paste --type image --watch cliphist store"],
        # cron job
        ["~/.config/hypr/script/cron_job.py"],
        # syncthing
        ["pidof syncthing || syncthing -no-browser"],
        # hyprshades
        ["hyprshade on blue-light-filter"],
]})

