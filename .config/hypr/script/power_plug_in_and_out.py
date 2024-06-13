#!/usr/bin/env python3
#####################################################################################
# don't put commands that runs for a long time here, it will block the main thread #
#####################################################################################


import json
import os
import subprocess

import pyudev

path = os.path.expanduser("~/.config/hypr/script/power_supply_cmds.json")


def cmd_to_call():
    file = open(path, "r")
    data = json.load(file)
    file.close()
    return data


def monitor_udev_events():
    global cmd_to_call_on_plug_in
    global cmd_to_call_on_plug_out
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem="power_supply")
    for device in iter(monitor.poll, None):
        if "POWER_SUPPLY_ONLINE" in device:
            power_supply_online = device.get("POWER_SUPPLY_ONLINE")
            if power_supply_online == "1":
                for cmds in cmd_to_call()["online"]:
                    subprocess.run(cmds, shell=True)
            else:
                for cmds in cmd_to_call()["offline"]:
                    subprocess.run(cmds, shell=True)


if __name__ == "__main__":
    print(f"""Running the script with the following path: {path}""")
    monitor_udev_events()
