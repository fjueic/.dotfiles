# layerrule = "blur", "waybar"
layerrule = "ignorezero", "waybar"
layerrule = "blurpopups", "waybar"
layerrule = "blur", "notifications"


windowrulev2 = "opacity 0.0 override 0.0 override", "class:(xwaylandvideobridge)$"
windowrulev2 = "noanim", "class:(xwaylandvideobridge)$"
windowrulev2 = "nofocus", "class:(xwaylandvideobridge)$"
windowrulev2 = "noinitialfocus", "class:(xwaylandvideobridge)$"

windowrulev2 = "float", "class:(org.pulseaudio.pavucontrol)$"
windowrulev2 = "size 1000 800", "class:(org.pulseaudio.pavucontrol)$"
windowrulev2 = "float", "class:(blueman-manager)$"
windowrulev2 = "size 1000 800", "class:(blueman-manager)$"
windowrulev2 = "float", "title:(Picture-in-Picture)$"
windowrulev2 = "float", "title:(File Operation Progress)$"
windowrulev2 = "float", "title:(Preferences)$"
windowrulev2 = "float", "title:(Confirm to replace files)$"
# windowrule = "nofocus", "title:.*main.*"
# windowrule = "noblur", "title:.*minimal.*"
# windowrule = "noborder", "title:.*minimal.*"

# windowrulev2="opacity 0.95 0.95 1","title:.*"
# windowrulev2="opacity 1 1 1","title:.*mpv"
# windowrulev2="opacity 1.0 override 1.0 override","title:(.*Wallpapers? - wallhaven\.cc.*)$"

windowrulev2 = "opacity 0.95 0.95 1", "class:(foot)"
windowrulev2 = "opacity 0.80 0.80", "class:(Rofi)"


# Workspace rules
for i in range(1, 7):
    workspace = f"{i},monitor:eDP-1"
# for i in range(1, 8):
#     workspace=f"{i},monitor:eDP-1"
for i in range(7, 10):
    workspace = f"{i},monitor:HEADLESS-2"
