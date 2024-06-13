from Hyprlang import *

conf = Hyprlang_config(__file__)
wallpaper = '/home/minoru/Desktop/wallpapers/cote/1716129018-removebg.png'
# wallpaper = '/home/minoru/Desktop/wallpapers/yamada/Akane_Kinoshita_Portrait.webp'

splash = 0
monitor =  ''

def restart_hyprpaper():
    from os import system
    system('killall hyprpaper')
    system('hyprpaper >/dev/null & disown')
def pre_process(wall):
    from os import system
    system(f"convert \"{wall}\" -resize 1920x1080 -background black -gravity center -extent 1920x1080 /tmp/hyprlang/wallpaper.png")

pre_process(wallpaper)
wallpaper = "/tmp/hyprlang/wallpaper.png"
conf.add_via_primitive(
    preload = [[wallpaper]],
    wallpaper = [[monitor, wallpaper]],
    splash = [[splash]],
)
conf.add_side_effect(restart_hyprpaper)
config = Hyprlang( '/tmp/hyprlang/hyprpaper.conf',__file__)
config.add(conf)
if __name__ == '__main__':
    config.write()
    config.watch()
    from time import sleep
    sleep(10**9)
