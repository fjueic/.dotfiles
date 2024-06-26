
from Hyprlang import *
conf = Hyprlang_config(__file__)
conf.add_via_primitive(
    monitor = [
        ['eDP-1', '1920x1080', '0x0', '1'],
        ['HEADLESS-2', '1280x720', '2000x2000', '1']
    ],
    env = [
        ['HYPRCURSOR_THEME', 'rose-pine-hyprcursor'],
        ['HYPRCURSOR_SIZE', '24'],
        ['XCURSOR_THEME', 'BreezeX-RosePineDawn-Linux'],
        ['XCURSOR_SIZE', '24'],
        ['MOZ_ENABLE_WAYLAND', '1']
    ],
    input = {
        'kb_layout':[ 'us'],
        'numlock_by_default':[ 'yes'],
        'repeat_rate':[ 50],
        'follow_mouse':[ 1],
        'touchpad': {
            'drag_lock':[ 'yes'],
            'disable_while_typing':[ 'yes'],
            'natural_scroll':[ 'no'],
        },
        'kb_options':[ 'ctrl:swapcaps'],
        # 'kb_options':[ 'altwin:swap_alt_win'],
        'sensitivity':[0 ]
    },
    general = {
        'gaps_in':[ 0],
        'gaps_out':[ 0],
        'border_size':[ 1],
        'col.active_border':[ 'rgba(FFC0CBee) rgba(FFFF33ee) 45deg'],
        'col.inactive_border':[ 'rgba(595959aa)'],
        'layout':[ 'dwindle'],
        'allow_tearing':[ 'false'],
    },
    decoration = {
        'blur': {
            'enabled':[ 0],
        }
    },
    animations = {
        'enabled':[ 0],
    },
    dwindle = {
        'pseudotile':[ 'yes'],
        'preserve_split':[ 'yes'],
        'no_gaps_when_only':[1]
    },
    gestures = {
        'workspace_swipe':[ 'on'],
        'workspace_swipe_fingers':[ 3],
    },
    misc = {
        'force_default_wallpaper':[ 0],
        'vfr':[ 'true'],
    }
)
config = Hyprlang( '/tmp/hyprlang/hyprland.conf',__file__)
import hyprbinds, hyprExecOnce
config.add(conf)
config.add(hyprbinds.config)
config.add(hyprExecOnce.config)


if __name__ == '__main__':
    config.write()
    config.watch()
    from time import sleep
    sleep(10**9)
