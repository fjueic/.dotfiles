from Hyprlang import RGBA
output="./hyprlock.conf"
_wallpaper = '/home/minoru/Desktop/jjk/sukuna-yuji-itadori-jujutsu-kaisen-4k-wallpaper-uhdpaper.com-593@0@e.jpg'
# wallpaper = '/home/minoru/Desktop/jjk/sukuna-itadori-jujutsu-kaisen-4k-wallpaper-uhdpaper.com-194@2@a.jpg'
_text_color = RGBA(255, 255, 255, 1)
_monitor = {"monitor": [""]}

def pre_process(wall):
    from os import system

    system(
        f'magick "{wall}" -resize 1920x1080 -background black -gravity center -extent 1920x1080 /tmp/hyprlang/lock_wallpaper.png'
    )

pre_process(_wallpaper)
_wallpaper = "/tmp/hyprlang/lock_wallpaper.png"
general={
    "no_fade_in": 1,
    "no_fade_out": 1,
}
background={
    **_monitor,
    "path": _wallpaper,
    "color": RGBA(25, 20, 20, 1.0),
    "blur_passes": 0,
    "blur_size": 2,
    "noise": 0.11,
}
label={
    **_monitor,
    "text": "cmd[update:1000] echo $TIME",
    "color": _text_color,
    "font_size": 70,
    "font_family": "Noto Sans",
    "position": (0, 90),
    "halign": "center",
    "valign": "center",
}
input_field={
    **_monitor,
    "size": (200, 50),
    "outline_thickness": 0,
    "inner_color": RGBA(150, 150, 150),
    "font_color": RGBA(10, 10, 10),
    "dots_center": "true",
    "color": RGBA(0, 0, 0, 0.8),
    "fade_on_empty": "true",
    "hide_input": "false",
    "position": (0, 0),
    "halign": "center",
    "valign": "bottom",
}




