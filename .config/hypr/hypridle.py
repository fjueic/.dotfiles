from Hyprlang import *
conf = Hyprlang_config(__file__)
conf.add_via_primitive(
    general = {
        'lock_cmd':[ 'pidof hyprlock ||  hyprlock'],
        'unlock_cmd':[ 'pkill -USR1 hyprlock'],
        'before_sleep_cmd':[ 'loginctl lock-session'],
        'after_sleep_cmd':[ '(kill $(pidof hypridle) || true) && (pidof hypridle || hypridle)'],
        'ignore_dbus_inhibit':[ False],
    },
    listener = [
        # Screenlock
        {
            'timeout':[ 300],
            'on-timeout':[ 'loginctl lock-session'],
        },
        # Suspend
        {
            'timeout':[ 600],
            'on-timeout':[ 'systemctl suspend'],
        }
    ]
)

config = Hyprlang("/tmp/hyprlang/hypridle.conf", __file__)
config.add(conf)

if __name__ == '__main__':
    config.write()
    config.watch()
    from time import sleep
    sleep(10**9)
