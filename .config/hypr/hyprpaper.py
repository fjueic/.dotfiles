from Hyprlang import *

conf = Hyprlang_config(__file__)
wallpaper = "/home/minoru/Desktop/yoimiya/yoimiya-genshin-impact-art-4k-wallpaper-3840x2160-uhdpaper.com-932.1_a.jpg"

monitor = ""


def restart_hyprpaper():
    from os import system

    system("killall hyprpaper")
    system("hyprpaper >/dev/null & disown")


def pre_process(wall):
    from os import system

    system(
        f'magick "{wall}" -resize 1920x1080 -background black -gravity center -extent 1920x1080 /tmp/hyprlang/wallpaper.png'
    )


pre_process(wallpaper)
wallpaper = "/tmp/hyprlang/wallpaper.png"
conf.add_config_entries(
    preload=(wallpaper),
    wallpaper=[(monitor, wallpaper)],
    splash=0,
)
conf.add_side_effect(restart_hyprpaper)
config = Hyprlang("/tmp/hyprlang/hyprpaper.conf", __file__)
config.add(conf)
if __name__ == "__main__":
    config.write()
    import subprocess

    command = [
        "bash",
        "-c",
        "(pidof hyprpaper || [ -f /tmp/hyprlang/hyprpaper.conf ] && hyprpaper)",
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
