from Hyprlang import *


output="./hyprland.conf"

monitor="eDP-1", "1920x1080", "0x0", "1"
monitor="HEADLESS-2", "1280x720", "2000x2000", "1"
# monitor="HEADLESS-2", "640x360", "2000x2000", "1"

env="XCURSOR_SIZE", "24"
env="MOZ_ENABLE_WAYLAND", "1"
input={
    "kb_layout": "us",
    "numlock_by_default": "yes",
    "repeat_rate": 50,
    "follow_mouse": 1,
    "touchpad": {
        "drag_lock": "yes",
        "disable_while_typing": "yes",
        "natural_scroll": "no",
    },
    "kb_options": "ctrl:swapcaps",
    # 'kb_options': 'altwin:swap_alt_win',
    # 'kb_options' : 'caps:ctrl_modifier',
    "sensitivity": 0,
}

cursor={
    "inactive_timeout": 10,
    "zoom_factor": 1,
    "hide_on_key_press": 1,
}
    
general={
    "gaps_in": 0,
    "gaps_out": 0,
    "border_size": 1,
    "col.active_border": Gradient(
        RGBA(255, 192, 203, 0.93).hex(), RGBA(255, 255, 51, 0.93).hex(), 45
    ),
    "col.inactive_border": "rgba(595959aa)",
    "col.inactive_border": RGBA(89, 89, 89, 0.67).hex(),
    "layout": "dwindle",
    "allow_tearing": "false",
}
# windowrulev2="opacity 0.95 0.95 1","title:.*"
# windowrulev2="opacity 1 1 1","title:.*mpv"
# windowrulev2="opacity 1.0 override 1.0 override","title:(.*Wallpapers? - wallhaven\.cc.*)$"
windowrulev2="opacity 0.95 0.95 1","title:.*foot*."
decoration={
    "blur": {
        "enabled": 1,
        "size": 3,
        "passes": 1,
    },
    "fullscreen_opacity": 1,
    "screen_shader":"~/.config/hypr/shaders/bluelight.frag",
}
animations={
    "enabled": 0,
}
dwindle={
    "pseudotile": "yes",
    "preserve_split": "yes",
}
gestures={
    "workspace_swipe": "on",
    "workspace_swipe_fingers": 3,
}
misc={
    "force_default_wallpaper": 0,
    "vfr": "true",
}

source="./hyprbinds.py"
source="./hyprExecOnce.py"


