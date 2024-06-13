#!/bin/python3

####################################################################
# Don't put commands that runs for a long time in this script.     #
# No cron job is used here. Hyprland will execute using exec-once. #
# Sleep is used instead of cron job.                               #
####################################################################

import hashlib
import json
import os
import subprocess
import time


def get_json_data(path):
    with open(path, "r") as f:
        return json.load(f)


def send_notification(message, urgency="normal"):
    subprocess.run(f"notify-send -u {urgency} '{message}'", shell=True)


def hash_data(obj):
    for cond in obj:
        for action in obj[cond]:
            for key in list(action.keys()):
                action["value"] = int(key)
                action["cmd"] = action.pop(key)
                hashobj = hashlib.sha256()
                hashobj.update((cond + key + action["cmd"]).encode())
                action["hash"] = hashobj.hexdigest()


def path_was_rewritten(
    path,
    previous_time,
):
    return previous_time != os.path.getmtime(path)


def get_battery_percentage():
    file = open("/sys/class/power_supply/BAT0/capacity", "r")
    percentage = file.read()
    file.close()
    return int(percentage)


def execute_cmd(action):
    if os.path.exists(f"/tmp/monitor_battery/{action['hash']}"):
        return
    print(action["cmd"])
    subprocess.run(action["cmd"], shell=True)
    open(f"/tmp/monitor_battery/{action['hash']}", "x").close()


def try_removing_file(t):
    t = f"/tmp/monitor_battery/{t}"
    if os.path.exists(t):
        os.remove(t)


def handle_battery(action, condition, bat):
    if eval(f"{bat} {condition} {action['value']}"):
        execute_cmd(action)
    else:
        try_removing_file(action["hash"])


def cycle(path, conf, written_time, bat):
    if not os.path.exists("/tmp/monitor_battery"):
        os.mkdir("/tmp/monitor_battery")
    for key in conf:
        for action in conf[key]:
            handle_battery(action, key, bat)


def main():
    path = os.path.expanduser("~/.config/hypr/script/monitor_battery_cmds.json")
    conf = None
    written_time = 0
    while True:
        time.sleep(60)
        if path_was_rewritten(path, written_time):
            try:
                get_json_data(path)
            except json.JSONDecodeError:
                send_notification(
                    "monitor_battery configuration is invalid", "critical"
                )
                continue
            conf = get_json_data(path)
            hash_data(conf)
            written_time = os.path.getmtime(path)
            if written_time != 0:
                send_notification("monitor_battery configuration has been updated")
        cycle(path, conf, written_time, get_battery_percentage())


if __name__ == "__main__":
    main()
