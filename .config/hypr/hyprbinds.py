from Hyprlang import *

config = Hyprlang_config(__file__)
mainMod = 'SUPER'
terminal = 'foot'
# terminal = 'kitty'
fileManager = 'nautilus'
menu = f'rofi -terminal {terminal} -show drun'

# some main things
config.add_via_primitive(
    bind = [
        [mainMod, 'RETURN', 'exec', terminal],
        [mainMod, 'C', 'exec', '~/.config/hypr/script/minimizeSteam.sh'],
        [mainMod, 'E', 'exec', fileManager],
        [mainMod, 'V', 'togglefloating'],
        [mainMod, 'R', 'exec', menu],
        [mainMod, 'P', 'pseudo'],
        [mainMod, 'O', 'togglesplit'],
        [mainMod, 'W', 'exec', 'firefox-developer-edition'],
        [mainMod, 'HOME', 'exit'],
    ]
)

# Move focus with mainMod + arrow keys
config.add_via_primitive(
    bind = [
        [mainMod, 'H', 'movefocus', 'l'],
        [mainMod, 'L', 'movefocus', 'r'],
        [mainMod, 'K', 'movefocus', 'u'],
        [mainMod, 'J', 'movefocus', 'd'],
    ]
)

# Moving windows
config.add_via_primitive(
    bind = [
        [f"{mainMod} SHIFT",'H', 'swapwindow', 'l'],
        [f"{mainMod} SHIFT",'L', 'swapwindow', 'r'],
        [f"{mainMod} SHIFT",'K', 'swapwindow', 'u'],
        [f"{mainMod} SHIFT",'J', 'swapwindow', 'd'],
    ]
)

# Window resizing
config.add_via_primitive(
    binde = [
        [f"{mainMod} CTRL",'H', 'resizeactive', Vec2(-60, 0)],
        [f"{mainMod} CTRL",'L', 'resizeactive', Vec2(60, 0)],
        [f"{mainMod} CTRL",'K', 'resizeactive', Vec2(0, -60)],
        [f"{mainMod} CTRL",'J', 'resizeactive', Vec2(0, 60)],
    ]
)

# change wallpaper between static and video
config.add_via_primitive(
    bind = [
        [f"{mainMod} SHIFT",'C', 'exec', '(pidof mpvpaper > /dev/null && killall mpvpaper && notify-send "Wallpaper changed to static") || (notify-send "Wallpaper changed to video" && mpvpaper -o "no-audio loop-file=\'inf\'" "*" \'/home/minoru/Desktop/wallpapers/yoimiya/1 [ZimHFN2wdEE].mkv\' &)'],
    ]
)

config.add_via_primitive(
    bind = [
        # ScreenShot with print
        ["", 'print', 'exec', '~/.config/hypr/script/screenshot.sh 1 && notify-send "ScreenShot Saved"'],
        ['ALT', 'print', 'exec', '~/.config/hypr/script/screenshot.sh && notify-send "ScreenShot Saved"'],
        # ScreenRecording with mainMod + print
        ['SUPER', 'print', 'exec', '~/.config/hypr/script/recorder.sh'],
    ]
)

config.add_via_primitive(
    bind = [
        # clipboard binding with mainMod + ` (backtick)
        [mainMod, 'grave', 'exec', '~/.config/hypr/script/copy.sh'],
        # hyprpicker
        [f"{mainMod} SHIFT",'P', 'exec', 'hyprpicker | wl-copy'],
        # monitor rotate
        [mainMod, 'Tab', 'focusmonitor', -1],
    ]
)

config.add_via_primitive(
    bind = [
        # Switch workspaces with mainMod + [0-9]
        *[ [mainMod, str(i%10), 'workspace', i] for i in range(1, 11) ],
        # Move active window to a workspace with mainMod + SHIFT + [0-9]
        *[ [f"{mainMod} SHIFT", str(i%10), 'movetoworkspace', i] for i in range(1, 11) ],
    ]
)

# Workspace rules
config.add_via_primitive(
    workspace = [
        *[[f'{i},monitor:eDP-1'] for i in range(1, 8)],
        *[[f'{i},monitor:HEADLESS-2'] for i in range(8, 11)],
    ]
)

# Special workspace (scratchpad)
config.add_via_primitive(
    bind = [
        [mainMod, 'S', 'togglespecialworkspace', 'magic'],
        [f"{mainMod} SHIFT",'S', 'movetoworkspace', 'special:magic'],
    ]
)

# Shutdown, reboot, lock, etc.
config.add_via_primitive(
    bind = [
        [mainMod, 'DELETE', 'exec', 'systemctl poweroff'],
        [mainMod, 'END', 'exec', 'systemctl reboot'],
        [mainMod, 'PAGE_DOWN', 'exec', 'systemctl suspend'],
        [mainMod, 'PAGE_UP', 'exec', 'loginctl lock-session'],
    ]
)

# Toggle fullscreen with mainMod + F
config.add_via_primitive(
    bind = [
        [mainMod, 'F', 'fullscreen'],
    ]
)

# Scroll through existing workspaces with mainMod + scroll
config.add_via_primitive(
    bind = [
        [mainMod, 'mouse_down', 'workspace', 'e+1'],
        [mainMod, 'mouse_up', 'workspace', 'e-1'],
    ]
)

# Move/resize windows with mainMod + LMB/RMB and dragging
config.add_via_primitive(
    bindm = [
        [mainMod, 'mouse:272', 'movewindow'],
        [mainMod, 'mouse:273', 'resizewindow'],
    ]
)

# Brightness and volume controls
config.add_via_primitive(
    bindel = [
        ['','XF86MonBrightnessUp', 'exec', 'brightnessctl set +10%'],
        ['','XF86MonBrightnessDown', 'exec', 'brightnessctl set 10%-'],
        ['','XF86AudioRaiseVolume', 'exec', 'pamixer -i 5'],
        ['','XF86AudioLowerVolume', 'exec', 'pamixer -d 5'],
        ['','XF86AudioMute', 'exec', 'pamixer -t'],
    ]
)

# Media keys
config.add_via_primitive(
    binde = [
        ['', 'XF86AudioPlay', 'exec', 'playerctl play-pause'],
        ['', 'XF86AudioNext', 'exec', 'playerctl next'],
        ['', 'XF86AudioPrev', 'exec', 'playerctl previous'],
    ]
)

# copy pdf dark mode code
config.add_via_primitive(
    bind = [
        ['CTRL+ALT', 'D', 'exec', 'cat ~/Obsidian/dark\ mode.js | wl-copy'],
    ]
)

# waybar
config.add_via_primitive(
    bind = [
        [mainMod, 'space', 'exec', 'pidof waybar >/dev/null && killall waybar || waybar'],
    ]
)

