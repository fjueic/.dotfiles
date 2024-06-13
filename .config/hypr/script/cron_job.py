#!/bin/python3


##################################################################
# Configs won't be automatically loaded, restart to apply changes #
##################################################################


from time import sleep
from subprocess import run

def load_data(path):
    import json
    try:
        with open(path, "r") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        from monitor_battery import send_notification
        send_notification("cron_job configuration is invalid", "critical")
        exit(1)

def value_to_int(data):
    return {k: int(v) for k, v in data.items()}


def main():
    import os
    path = os.path.expanduser("~/.config/hypr/script/cron_job.json")
    del os
    data = value_to_int(load_data(path))
    data["ls > /dev/null"] = 10**9
    original_data = data.copy()
    while True:
        for k, v in data.items():
            if v == 0:
                run(k, shell=True)
                data[k] = original_data[k]
        minimum = sorted(data.values())[0]
        for k, v in data.items():
            data[k] = v - minimum
        sleep(minimum)


if __name__ == "__main__":
    main()
