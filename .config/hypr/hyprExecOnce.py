from Hyprlang import *

config = Hyprlang_config(__file__)
config.add_config_entries(
    **{
        "exec-once": [
            # lock on boot
            "[ -f /tmp/hyprlang/hyprlock.conf ] && (hyprlock || hyprctl dispatch exit)",
            # create virtual monitor
            "hyprctl output create headless",
            # wayvnc
            "pidof wayvnc || wayvnc -g 0.0.0.0",
            # hypridle
            "(killall hypridle || true) && hypridle",
            "(pidof waybar || waybar)",
            "(pidof hyprpaper || [ -f /tmp/hyprlang/hyprpaper.conf ] && hyprpaper)",
            "/usr/lib/polkit-kde-authentication-agent-1",
            "gnome-keyring-daemon --start --components=secrets",
            "blueman-applet",
            "nm-applet --indicator",
            "/usr/lib/kdeconnectd",
            "/usr/bin/kdeconnect-indicator",
            "~/.config/hypr/script/change_all_mice_state.sh on",
            "~/.config/hypr/script/spin_up_markdown_preview_server.sh",
            # commands to run when the power plug is plugged in or out
            "~/.config/hypr/script/power_plug_in_and_out.py",
            # battery monitor
            "~/.config/hypr/script/monitor_battery.py",
            # clipboard manager
            "wl-paste --type text --watch cliphist store",
            "wl-paste --type image --watch cliphist store",
            # cron job
            "~/.config/hypr/script/cron_job.py",
            # syncthing
            "pidof syncthing || syncthing -no-browser",
            # hyprshades
            "hyprshade on blue-light-filter",
            # will name later
            "cd ~/.config/hypr/ && python hypridle.py",
            "cd ~/.config/hypr/ && python hyprlock.py",
            "cd ~/.config/hypr/ && python hyprpaper.py",
            # screen sharing
            "dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP",
        ]
    }
)
