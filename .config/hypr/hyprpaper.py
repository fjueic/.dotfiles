output="./hyprpaper.conf"
_wallpaper = '/home/minoru/Desktop/yoimiya/yoimiya-genshin-impact-art-4k-wallpaper-3840x2160-uhdpaper.com-932.1_a.jpg'
# _wallpaper = '/home/minoru/Desktop/jjk/sukuna-itadori-jujutsu-kaisen-4k-wallpaper-uhdpaper.com-194@2@a.jpg'

_monitor = ""
def restart_hyprpaper():
    from os import system
    system("killall hyprpaper")
    system("hyprpaper >/dev/null & disown")

preload=_wallpaper
wallpaper=_monitor, _wallpaper
splash=0
restart_hyprpaper()
