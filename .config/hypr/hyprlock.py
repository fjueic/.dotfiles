from Hyprlang import *

conf = Hyprlang_config(__file__)
wallpaper = '/home/minoru/Desktop/jjk/sukuna-yuji-itadori-jujutsu-kaisen-4k-wallpaper-uhdpaper.com-593@0@e.jpg'
# wallpaper = '/home/minoru/Desktop/jjk/sukuna-itadori-jujutsu-kaisen-4k-wallpaper-uhdpaper.com-194@2@a.jpg'

text_color = RGBA(255, 255, 255, 1)
monitor = {"monitor": [""]}


def pre_process(wall):
    from os import system

    system(
        f'convert "{wall}" -resize 1920x1080 -background black -gravity center -extent 1920x1080 /tmp/hyprlang/lock_wallpaper.png'
    )


pre_process(wallpaper)
wallpaper = "/tmp/hyprlang/lock_wallpaper.png"
conf.add_config_entries(
    general={
        "no_fade_in": 1,
        "no_fade_out": 1,
    }, background={
        **monitor,
        "path": wallpaper,
        "color": RGBA(25, 20, 20, 1.0),
        "blur_passes": 0,
        "blur_size": 2,
        "noise": 0.11,
    },
    label={
        **monitor,
        "text": "cmd[update:1000] echo $TIME",
        "color": text_color,
        "font_size": 70,
        "font_family": "Noto Sans",
        "position": (0, 90),
        "halign": "center",
        "valign": "center",
    },
    **{
        "input-field": {
            **monitor,
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
    },
)

config = Hyprlang("/tmp/hyprlang/hyprlock.conf", __file__)
config.add(conf)
if __name__ == "__main__":
    config.write()
    import subprocess

    command = [
        "bash",
        "-c",
        "[ -f /tmp/hyprlang/hyprlock.conf ] && (hyprlock || hyprctl dispatch exit)",
    ]
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        close_fds=True,
    )
    config.watch()
    from time import sleep

    sleep(10**9)
