output="hypridle.conf"
_lock_cmd = "pidof hyprlock ||  hyprlock"
_unlock_cmd = "pkill -USR1 hyprlock"
general={
    "lock_cmd": _lock_cmd,
    "unlock_cmd": _unlock_cmd,
    "before_sleep_cmd": f"loginctl lock-session || {_lock_cmd}",
    "after_sleep_cmd": "(kill $(pidof hypridle) || true) && (pidof hypridle || hypridle)",
    # "ignore_dbus_inhibit": 0,
}
listener={
    "timeout": 300,
    "on-timeout": f"loginctl lock-session || {_lock_cmd}",
}
listener={
    "timeout": 600,
    "on-timeout": "systemctl suspend",
}

