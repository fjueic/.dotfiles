from Hyprlang import Vec2
from hypridle import _lock_cmd
_mainMod = "SUPER"
# _mainMod = "CTRL ALT SHIFT"
_terminal = "foot"
# _terminal = 'kitty'
_fileManager = "nautilus"
_fileManager = f"{_terminal} ranger"
_menu = f"rofi -terminal {_terminal} -show drun"
_mainMod_SHIFT = f"{_mainMod} SHIFT"
_exec = "exec"
_movefocus = "movefocus"
_mainMod_CTRL = f"{_mainMod} CTRL"
_swapwindow = "swapwindow"
_resizeactive = "resizeactive"
_left = "left"
_right = "right"
_up = "up"
_down = "down"



# bind=_mainMod,"A",_exec,"notify-send 'Hello, World!'"

# Keybinds
bind=_mainMod,"G",_exec,"cat ~/information.txt | rofi -dmenu | wl-copy"
bind="CTRL SHIFT","Y",_exec,"wl-paste | wtype -"
bind=_mainMod,"RETURN",_exec,_terminal
bind=_mainMod,"C",_exec,"~/.config/hypr/script/minimizeSteam.sh"
bind=_mainMod,"E",_exec,_fileManager
bind=_mainMod,"V","togglefloating"
bind=_mainMod,"R",_exec,_menu
bind=_mainMod,"P","pseudo"
bind=_mainMod,"O","togglesplit"
bind=_mainMod,"W",_exec,"firefox-developer-edition"
bind=_mainMod,"HOME","exit"
bind=_mainMod,"F","fullscreen"
# Move focus with mainMod + arrow keys
bind=_mainMod,"H",_movefocus,"l"
bind=_mainMod,"L",_movefocus,"r"
bind=_mainMod,"K",_movefocus,"u"
bind=_mainMod,"J",_movefocus,"d"
bind=_mainMod,_left,_movefocus,"l"
bind=_mainMod,_right,_movefocus,"r"
bind=_mainMod,_up,_movefocus,"u"
bind=_mainMod,_down,_movefocus,"d"
# Moving windows
bind=_mainMod_SHIFT,"H",_swapwindow,"l"
bind=_mainMod_SHIFT,"L",_swapwindow,"r"
bind=_mainMod_SHIFT,"K",_swapwindow,"u"
bind=_mainMod_SHIFT,"J",_swapwindow,"d"
bind=_mainMod_SHIFT,_left,_swapwindow,"l"
bind=_mainMod_SHIFT,_right,_swapwindow,"r"
bind=_mainMod_SHIFT,_up,_swapwindow,"u"
bind=_mainMod_SHIFT,_down,_swapwindow,"d"
# Window resizing
binde=_mainMod_CTRL,"H",_resizeactive,Vec2(-60, 0)
binde=_mainMod_CTRL,"L",_resizeactive,Vec2(60, 0)
binde=_mainMod_CTRL,"K",_resizeactive,Vec2(0, -60)
binde=_mainMod_CTRL,"J",_resizeactive,Vec2(0, 60)
binde=_mainMod_CTRL,_left,_resizeactive,Vec2(-60, 0)
binde=_mainMod_CTRL,_right,_resizeactive,Vec2(60, 0)
binde=_mainMod_CTRL,_up,_resizeactive,Vec2(0, -60)
binde=_mainMod_CTRL,_down,_resizeactive,Vec2(0, 60)

# change wallpaper between static and video
# bindl = _mainMod_SHIFT,"C",_exec,'(pidof mpvpaper > /dev/null && killall mpvpaper && notify-send "Wallpaper changed to static") || (notify-send "Wallpaper changed to video" && mpvpaper -o "no-audio loop-file=\'inf\'" "*" \'/home/minoru/Desktop/wallpapers/yoimiya/1 [ZimHFN2wdEE].mkv\' &)'

# ScreenShot with print
bindl="","print",_exec,'~/.config/hypr/script/screenshot.sh 1 && notify-send "ScreenShot Saved"'
bindl="ALT","print",_exec,'~/.config/hypr/script/screenshot.sh && notify-send "ScreenShot Saved"'
bindl=_mainMod,"print",_exec,'~/.config/hypr/script/recorder.sh'

# clipboard binding with mainMod + ` (backtick)
bind=_mainMod,"grave",_exec,'~/.config/hypr/script/copy.sh'
# hyprpicker
bind=_mainMod_SHIFT,"P",_exec,'hyprpicker | wl-copy'
# monitor rotate
bind=_mainMod,"Tab","focusmonitor",-1

for i in range(1, 11):
    # Switch workspaces with mainMod + [0-9]
    bind=_mainMod,str(i % 10),"workspace",i
    # Move active window to a workspace with mainMod + SHIFT + [0-9]
    bind=_mainMod_SHIFT,str(i % 10),"movetoworkspace",i

# Workspace rules
for i in range(1,11):
    workspace=f"{i},monitor:eDP-1"
# for i in range(1, 8):
#     workspace=f"{i},monitor:eDP-1"
# for i in range(8, 11):
#     workspace=f"{i},monitor:HEADLESS-2"

# Special workspace (scratchpad)
bind=_mainMod,"S","togglespecialworkspace","magic"
bind=_mainMod_SHIFT,"S","movetoworkspace","special:magic"

# Shutdown, reboot, lock, etc.
bind=_mainMod,"DELETE",_exec,"systemctl poweroff"
bind=_mainMod,"END",_exec,"systemctl reboot"
bind=_mainMod,"PAGE_DOWN",_exec,"systemctl suspend"
bind=_mainMod,"PAGE_UP",_exec,f"loginctl lock-session || {_lock_cmd}"
bind=_mainMod,"INSERT","forcerendererreload"

# Scroll through existing workspaces with mainMod + scroll
bind=_mainMod,"mouse_down","workspace","e+1"
bind=_mainMod,"mouse_up","workspace","e-1"

# Move/resize windows with mainMod + LMB/RMB and dragging
bindm=_mainMod,"mouse:272","movewindow"
bindm=_mainMod,"mouse:273","resizewindow"

# Brightness and volume controls
bindel="","XF86MonBrightnessUp",_exec,"brightnessctl set +10%"
bindel="","XF86MonBrightnessDown",_exec,"brightnessctl set 10%-"
bindel="","XF86AudioRaiseVolume",_exec,"pamixer -i 5"
bindel="","XF86AudioLowerVolume",_exec,"pamixer -d 5"
bindel="","XF86AudioMute",_exec,"pamixer -t"

# Media keys
binde="","XF86AudioPlay",_exec,"playerctl play-pause"
binde="","XF86AudioNext",_exec,"playerctl next"
binde="","XF86AudioPrev",_exec,"playerctl previous"

# copy pdf dark mode code
bind="CTRL+ALT","D",_exec,r"cat ~/Obsidian/dark\ mode.js | wl-copy"

# waybar
bind=_mainMod,"space",_exec,"pidof waybar >/dev/null && killall waybar || waybar"

# display on and off
bindl=_mainMod,"d",_exec,"sleep 1 && hyprctl dispatch dpms off"
bindl=_mainMod,"u",_exec,"sleep 1 && hyprctl dispatch dpms on"

# zoom
_get_zoom="hyprctl getoption cursor:zoom_factor | grep float"
_notifier_zoom=_get_zoom+" | awk '{print $2}'"+" | xargs notify-send -t 1000"

_zoom_in=(
    f"{_get_zoom} | awk "
    "'"
    '{ system("hyprctl keyword cursor:zoom_factor " $2 + 0.1) }'
    "'"
)

_zoom_out=(
    f"{_get_zoom} | awk "
    "'"
    '{if($2!=1) system("hyprctl keyword cursor:zoom_factor " $2 - 0.1) }'
    "'"
)

binde=_mainMod,"minus",_exec,_zoom_out+" && "+_notifier_zoom
binde=_mainMod,"equal",_exec,_zoom_in+" && "+_notifier_zoom


