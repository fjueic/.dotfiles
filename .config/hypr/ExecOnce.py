# lock on boot
exec_once="(hyprlock || hyprctl dispatch exit)"
# create virtual monitor
# exec_once="hyprctl output create headless"
# wayvnc
# exec_once="pidof wayvnc || wayvnc -g 0.0.0.0"
# hypridle
exec_once="(killall hypridle || true) && hypridle"
exec_once="(pidof waybar || waybar)"
exec_once="(pidof hyprpaper || hyprpaper )"
exec_once="systemctl --user start plasma-polkit-agent"
exec_once="gnome-keyring-daemon --start --components=secrets"
exec_once="blueman-applet"
exec_once="nm-applet --indicator"
exec_once="/usr/lib/kdeconnectd"
exec_once="/usr/bin/kdeconnect-indicator"
exec_once="~/.config/hypr/script/change_all_mice_state.sh on"
exec_once="~/.config/hypr/script/spin_up_markdown_preview_server.sh"
# commands to run when the power plug is plugged in or out
exec_once="~/.config/hypr/script/power_plug_in_and_out.py"
# battery monitor
exec_once="~/.config/hypr/script/monitor_battery.py"
# clipboard manager
exec_once="wl-paste --type text --watch cliphist store"
exec_once="wl-paste --type image --watch cliphist store"
# cron job
exec_once="~/.config/hypr/script/cron_job.py"
# syncthing
exec_once="pidof syncthing || syncthing -no-browser"
# hyprshades
exec_once="hyprshade on blue-light-filter"
# will name later
# exec_once="cd ~/.config/hypr/ && python hypridle.py"
# exec_once="cd ~/.config/hypr/ && python hyprlock.py"
# exec_once="cd ~/.config/hypr/ && python hyprpaper.py"
exec_once= "cd ~/.dotfiles/.config/hypr/ && python Hyprlang.py ./hypridle.py ./hyprland.py ./hyprlock.py ./hyprpaper.py "
# screen sharing
exec_once="dbus-update-activation-environment --systemd wayland_display xdg_current_desktop"
exec_once="~/.config/hypr/script/slideshow.sh ~/Desktop/wallpaper"
exec_once="hyprsunset -t 20000K"

