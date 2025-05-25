from Hyprlang import *

output = "~/.config/hypr/hyprland.conf"
raw_text = "source = ./wallust.conf"

monitor = "eDP-1", "1920x1080", "0x0", "1"
monitor = "HEADLESS-2", "1280x720", "2000x2000", "1"
# monitor="HEADLESS-2", "640x360", "2000x2000", "1"

env = "XCURSOR_SIZE", "24"
env = "MOZ_ENABLE_WAYLAND", "1"
env = "TERM", "foot"

input = {
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

cursor = {
    "inactive_timeout": 10,
    "zoom_factor": 1,
    "hide_on_key_press": 1,
}

general = {
    "gaps_in": "0",
    "gaps_out": "0",
    "border_size": 1,
    # "col.active_border": Gradient(
    #     RGBA(255, 192, 203, 0.93).hex(), RGBA(255, 255, 51, 0.93).hex(), 45
    # ),
    "col.active_border": "$color1 $color2 $color3",
    "col.inactive_border": RGBA(89, 89, 89, 0.67).hex(),
    "layout": "dwindle",
    "allow_tearing": "false",
    "resize_on_border": 1,
}
decoration = {
    "rounding": 0,
    "blur": {
        "enabled": 1,
        "size": 3,
        "passes": 1,
    },
    "fullscreen_opacity": 1,
    # "screen_shader": "~/.config/hypr/shaders/bluelight.frag",
    # "screen_shader": "~/.config/hypr/shaders/crt.frag",
    # "screen_shader": "~/.config/hypr/shaders/test.frag",
}

animations = {
    "enabled": 0,
    # Animation curves
    "bezier": [
        ("linear", 0, 0, 1, 1),
        ("md3_standard", 0.2, 0, 0, 1),
        ("md3_decel", 0.05, 0.7, 0.1, 1),
        ("md3_accel", 0.3, 0, 0.8, 0.15),
        ("overshot", 0.05, 0.9, 0.1, 1.1),
        ("crazyshot", 0.1, 1.5, 0.76, 0.92),
        ("hyprnostretch", 0.05, 0.9, 0.1, 1.0),
        ("fluent_decel", 0.1, 1, 0, 1),
        ("easeInOutCirc", 0.85, 0, 0.15, 1),
        ("easeOutCirc", 0, 0.55, 0.45, 1),
        ("easeOutExpo", 0.16, 1, 0.3, 1),
    ],
    # Animation configs
    "animation": [
        ("windows", 1, 3, "md3_decel", "popin 60%"),
        ("border", 1, 10, "default"),
        ("fade", 1, 2.5, "md3_decel"),
        # ("workspaces", 1, 3.5, md3_decel, slide),
        ("workspaces", 1, 3.5, "easeOutExpo", "slide"),
        # ("workspaces", 1, 7, fluent_decel, slidefade 15%),
        # ("specialWorkspace", 1, 3, md3_decel, slidefadevert 15%),
        ("specialWorkspace", 1, 3, "md3_decel", "slidevert"),
        ("layers", 1, 3, "fluent_decel", "popin 60%"),
    ],
}

dwindle = {
    "pseudotile": "yes",
    "preserve_split": "yes",
}
gestures = {
    "workspace_swipe": "on",
    "workspace_swipe_fingers": 3,
    "workspace_swipe_forever": 1,
}
misc = {
    "force_default_wallpaper": 0,
    "vfr": "true",
}
ecosystem = {"no_update_news": 1}


source = "./binds.py"
source = "./ExecOnce.py"
source = "./rules.py"
