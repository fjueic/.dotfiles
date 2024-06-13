#!/bin/bash

if [ -f "/tmp/recording.lock" ]; then
    rm /tmp/recording.lock
    killall wf-recorder
    notify-send "Screen recording saved"
    exit 0
fi


sl=$(slurp)
video_path=~/Videos/Recordings/$(date +%s).mp4
touch "/tmp/recording.lock"
notify-send 'Screen recording started'
wf-recorder -g "$sl" -f "$video_path"  &
