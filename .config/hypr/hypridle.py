output="./hypridle.conf"
general={
    "lock_cmd": "pidof hyprlock ||  hyprlock",
    "unlock_cmd": "pkill -USR1 hyprlock",
    "before_sleep_cmd": "loginctl lock-session",
    "after_sleep_cmd": "(kill $(pidof hypridle) || true) && (pidof hypridle || hypridle)",
    # "ignore_dbus_inhibit": False,
}
listener={
    "timeout": 300,
    "on-timeout": "loginctl lock-session",
}
listener={
    "timeout": 600,
    "on-timeout": "systemctl suspend",
}

