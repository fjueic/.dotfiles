#!/bin/bash

# Ensure jq is installed
command -v jq >/dev/null 2>&1 || {
  echo >&2 "jq is required but not installed."; exit 1;
}

echo "Listening for notifications..."

# Start monitoring notifications
dbus-monitor "interface='org.freedesktop.Notifications',member='Notify'" |
awk -v q="'" '
  BEGIN {
    collecting = 0;
    count = 0;
  }

  /method call/ {
    collecting = 0;
    count = 0;
    delete args;
  }

  /member=Notify/ {
    collecting = 1;
    count = 0;
    delete args;
  }

  collecting && /string/ {
    match($0, /"([^"]*)"/, m);
    if (m[1] != "") {
      args[count++] = m[1];
    } else {
      args[count++] = "";
    }
  }

  collecting && /int32/ {
    match($0, /int32 (-?[0-9]+)/, m);
    args[count++] = m[1];
  }

  collecting && count == 8 {
    # Emit data to jq to construct safe JSON
    cmd = "jq -n --arg app_name \"" args[0] "\" " \
             "--arg replaces_id \"" args[1] "\" " \
             "--arg app_icon \"" args[2] "\" " \
             "--arg summary \"" args[3] "\" " \
             "--arg body \"" args[4] "\" " \
             "--arg actions \"" args[5] "\" " \
             "--arg hints \"" args[6] "\" " \
             "--arg expire_timeout \"" args[7] "\" " \
             "'\''{" \
             "app_name: $app_name, " \
             "replaces_id: ($replaces_id | tonumber), " \
             "app_icon: $app_icon, " \
             "summary: $summary, " \
             "body: $body, " \
             "actions: $actions, " \
             "hints: $hints, " \
             "expire_timeout: ($expire_timeout | tonumber)" \
             "}'\''"
    system(cmd)
    collecting = 0;
    count = 0;
    delete args;
  }
'


