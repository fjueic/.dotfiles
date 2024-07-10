from Hyprlang import *

conf = Hyprlang_config(__file__)
wallpaper = '/home/minoru/Desktop/wallpapers/cote/1716129018-removebg.png'
# wallpaper = '/home/minoru/Desktop/wallpapers/nino/41626439-638f-4730-8f6b-b18ab4d7f158.jpeg'
# wallpaper = '/home/minoru/Desktop/wallpapers/yamada/Akane_Kinoshita_Portrait.webp'
# wallpaper = '/home/minoru/Desktop/wallpapers/dragonball/340761.jpg'
# wallpaper = '/home/minoru/Desktop/wallpapers/yoimiya/ilovesakuya_稻妻冰x火_108867401/ilovesakuya_稻妻冰x火_108867401_p0.jpg'

splash = 0
monitor =  ''

def restart_hyprpaper():
    from os import system
    system('killall hyprpaper')
    system('hyprpaper >/dev/null & disown')
def pre_process(wall):
    from os import system
    system(f"magick \"{wall}\" -resize 1920x1080 -background black -gravity center -extent 1920x1080 /tmp/hyprlang/wallpaper.png")

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
    import subprocess
    command = ["bash", "-c", "(pidof hyprpaper || [ -f /tmp/hyprlang/hyprpaper.conf ] && hyprpaper)"]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, close_fds=True)
    config.watch()
    from time import sleep
    sleep(10**9)
